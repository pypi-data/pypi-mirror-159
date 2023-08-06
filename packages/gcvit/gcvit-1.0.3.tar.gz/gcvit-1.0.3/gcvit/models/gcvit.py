import numpy as np
import tensorflow as tf

from ..layers import PatchEmbed, GCViTLayer, Identity


BASE_URL = 'https://github.com/awsaf49/gcvit-tf/releases/download'
TAG = 'v1.0.0'
NAME2CONFIG = {
    'gcvit_tiny': {'window_size': (7, 7, 14, 7),
                    'dim': 64,
                    'depths': (3, 4, 19, 5),
                    'num_heads': (2, 4, 8, 16), 
                    'path_drop': 0.2,},
    'gcvit_small': {'window_size': (7, 7, 14, 7), 
                     'dim': 96, 
                     'depths': (3, 4, 19, 5),
                     'num_heads': (3, 6, 12, 24),
                     'mlp_ratio': 2.,
                     'path_drop': 0.3,
                     'layer_scale': 1e-5,},
    'gcvit_base': {'window_size': (7, 7, 14, 7),
                    'dim':128, 
                    'depths': (3, 4, 19, 5),
                    'num_heads': (4, 8, 16, 32),
                    'mlp_ratio': 2.,
                    'path_drop': 0.5,
                    'layer_scale': 1e-5,},
    }

@tf.keras.utils.register_keras_serializable(package='gcvit')
class GCViT(tf.keras.Model):
    def __init__(self, window_size, dim, depths, num_heads,
        drop_rate=0., mlp_ratio=3., qkv_bias=True, qk_scale=None, attn_drop=0., path_drop=0.1, layer_scale=None, resize_query=False,
        pooling='avg', classes=1000, classifier_activation='softmax', **kwargs):
        super().__init__(**kwargs)
        self.window_size = window_size
        self.dim = dim
        self.depths = depths
        self.num_heads = num_heads
        self.drop_rate = drop_rate
        self.mlp_ratio = mlp_ratio
        self.qkv_bias = qkv_bias
        self.qk_scale = qk_scale
        self.attn_drop = attn_drop
        self.path_drop = path_drop
        self.layer_scale = layer_scale
        self.resize_query = resize_query
        self.pooling = pooling
        self.classes = classes
        self.classifier_activation = classifier_activation

        self.patch_embed = PatchEmbed(dim=dim, name='patch_embed')
        self.pos_drop = tf.keras.layers.Dropout(drop_rate, name='pos_drop')
        path_drops = np.linspace(0., path_drop, sum(depths))
        keep_dims = [(False, False, False),(False, False),(True,),(True,),]
        self.levels = []
        for i in range(len(depths)):
            path_drop = path_drops[sum(depths[:i]):sum(depths[:i + 1])].tolist()
            level = GCViTLayer(depth=depths[i], num_heads=num_heads[i], window_size=window_size[i], keep_dims=keep_dims[i],
                    downsample=(i < len(depths) - 1), mlp_ratio=mlp_ratio, qkv_bias=qkv_bias, qk_scale=qk_scale, 
                    drop=drop_rate, attn_drop=attn_drop, path_drop=path_drop, layer_scale=layer_scale, resize_query=resize_query,
                    name=f'levels/{i}')
            self.levels.append(level)
        self.norm = tf.keras.layers.LayerNormalization(axis=-1, epsilon=1e-05, name='norm')
        if pooling == 'avg':
            self.pool = tf.keras.layers.GlobalAveragePooling2D(name='pool')
        elif pooling == 'max':
            self.pool = tf.keras.layers.GlobalMaxPooling2D(name='pool')
        elif pooling is None:
            self.pool = Identity(name='pool')
        else:
            raise ValueError(f'Expecting pooling to be one of None/avg/max. Found: {pooling}')
        self.head = tf.keras.layers.Dense(classes, activation=classifier_activation, name='head')

    def feature(self, inputs, **kwargs):
        x = self.patch_embed(inputs)
        x = self.pos_drop(x)
        for level in self.levels:
            x = level(x)
        x = self.norm(x)
        x = self.pool(x)
        return x

    def call(self, inputs, **kwargs):
        x = self.feature(inputs)
        x = self.head(x)
        return x

    def build_graph(self, input_shape=(224, 224, 3)):
        """https://www.kaggle.com/code/ipythonx/tf-hybrid-efficientnet-swin-transformer-gradcam"""
        x = tf.keras.Input(shape=input_shape)
        return tf.keras.Model(inputs=[x], outputs=self.call(x), name=self.name)

# load standard models
def GCViTTiny(pretrain=False, **kwargs):
    name = 'gcvit_tiny'
    config = NAME2CONFIG[name]
    ckpt_link = '{}/{}/{}_weights.h5'.format(BASE_URL, TAG, name)
    model = GCViT(name=name, **config, **kwargs)
    model(tf.random.uniform(shape=(1, 224, 224, 3)))
    if pretrain:
        ckpt_path = tf.keras.utils.get_file('{}_weights.h5'.format(name), ckpt_link)
        model.load_weights(ckpt_path)
    return model

def GCViTSmall(pretrain=False, **kwargs):
    name = 'gcvit_small'
    config = NAME2CONFIG[name]
    ckpt_link = '{}/{}/{}_weights.h5'.format(BASE_URL, TAG, name)
    model = GCViT(name=name, **config, **kwargs)
    model(tf.random.uniform(shape=(1, 224, 224, 3)))
    if pretrain:
        ckpt_path = tf.keras.utils.get_file('{}_weights.h5'.format(name), ckpt_link)
        model.load_weights(ckpt_path)
    return model

def GCViTBase(pretrain=False, **kwargs):
    name = 'gcvit_base'
    config = NAME2CONFIG[name]
    ckpt_link = '{}/{}/{}_weights.h5'.format(BASE_URL, TAG, name)
    model = GCViT(name=name, **config, **kwargs)
    model(tf.random.uniform(shape=(1, 224, 224, 3)))
    if pretrain:
        ckpt_path = tf.keras.utils.get_file('{}_weights.h5'.format(name), ckpt_link)
        model.load_weights(ckpt_path)
    return model
