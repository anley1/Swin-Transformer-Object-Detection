_base_ = [
    './faster_rcnn_r50_fpn.py',
    '../_base_/datasets/bead_cropped_type_6_mask.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
