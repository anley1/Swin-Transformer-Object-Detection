_base_ = './htc_r50_fpn_1x_coco.py'
model = dict(
    pretrained='open-mmlab://resnext101_32x4d',
    backbone=dict(
        type='ResNeXt',
        depth=101,
        groups=32,
        base_width=4,
        num_stages=4,
        out_indices=(0, 1, 2, 3),
        frozen_stages=1,
        norm_cfg=dict(type='BN', requires_grad=True),
        norm_eval=True,
        style='pytorch'))
data = dict(samples_per_gpu=1, workers_per_gpu=1)
# learning policy
lr_config = dict(step=[16, 19])
runner = dict(type='EpochBasedRunner', max_epochs=30)

optimizer_config = dict(_delete_=True,
                        grad_clip=dict(max_norm=35.0, norm_type=2))
