# TODO: It would be nice to create keys here as: make_pretrained_model_key(Models.RESNET18, Dataset.COCO)
# TODO: Not only this would reduce risk of making a typo error, it would bring more clarity how the key is created
# TODO: And allow to "query" pretrained models by dataset
MODEL_URLS = {
    # RegNet-s
    "regnetY800_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/RegnetY800/average_model.pth",
    "regnetY600_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/RegnetY600/average_model_regnety600.pth",
    "regnetY400_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/RegnetY400/average_model_regnety400.pth",
    "regnetY200_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/RegnetY200/average_model_regnety200.pth",
    # ResNet-s
    "resnet50_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/KD_ResNet50_Beit_Base_ImageNet/resnet.pth",
    "resnet34_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/resent_34/average_model.pth",
    "resnet18_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/resnet18/average_model.pth",
    #
    "repvgg_a0_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/repvgg_a0_imagenet.pth",
    #
    "shelfnet34_lw_coco_segmentation_subclass": "https://deci-pretrained-models.s3.amazonaws.com" "/shelfnet34_coco_segmentation_subclass.pth",
    #
    "ddrnet_23_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ddrnet/cityscapes/ddrnet23_cwd/average_model.pth",
    "ddrnet_23_slim_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ddrnet/cityscapes/ddrnet23_slim_cwd/ckpt_best.pth",
    "ddrnet_39_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ddrnet/cityscapes/ddrnet39_al/average_model_2023_02_20.pth",
    #
    "stdc1_seg50_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/cityscapes_stdc1_seg50_dice_edge/ckpt_best.pth",
    "stdc1_seg75_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/stdc1_seg75_cityscapes/ckpt_best.pth",
    "stdc2_seg50_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/cityscapes_stdc2_seg50_dice_edge/ckpt_best.pth",
    "stdc2_seg75_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/stdc2_seg75_cityscapes/ckpt_best.pth",
    #
    "efficientnet_b0_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/efficientnet_b0/average_model-3.pth",
    #
    "ssd_lite_mobilenet_v2_coco": "https://deci-pretrained-models.s3.amazonaws.com/ssd_lite_mobilenet_v2/coco2017/2022-11-28/average_model.pth",
    "ssd_mobilenet_v1_coco": "https://deci-pretrained-models.s3.amazonaws.com/ssd_mobilenet_v1_coco_res320/ckpt_best.pth",
    #
    "mobilenet_v3_large_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/mobilenetv3+large+300epoch/average_model.pth",
    "mobilenet_v3_small_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/mobilenetv3+small/ckpt_best.pth",
    "mobilenet_v2_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/mobilenetv2+w1/ckpt_best.pth",
    #
    "regseg48_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/regseg48_cityscapes/ckpt_best.pth",
    #
    "vit_base_imagenet21k": "https://deci-pretrained-models.s3.amazonaws.com/vit_pretrained_imagenet21k/vit_base_16_imagenet21K.pth",
    "vit_large_imagenet21k": "https://deci-pretrained-models.s3.amazonaws.com/vit_pretrained_imagenet21k/vit_large_16_imagenet21K.pth",
    "vit_base_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/vit_base_imagenet1k/ckpt_best.pth",
    "vit_large_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/vit_large_cutmix_randaug_v2_lr%3D0.03/average_model.pth",
    #
    "beit_base_patch16_224_imagenet": "https://deci-pretrained-models.s3.amazonaws.com/beit_base_patch16_224_imagenet.pth",
    "beit_base_patch16_224_cifar10": "https://deci-pretrained-models.s3.amazonaws.com/beit_cifar10.pth",
    #
    "yolox_s_coco": "https://deci-pretrained-models.s3.amazonaws.com/yolox_coco/yolox_s_coco/average_model.pth",
    "yolox_m_coco": "https://deci-pretrained-models.s3.amazonaws.com/yolox_coco/yolox_m_coco/average_model.pth",
    "yolox_l_coco": "https://deci-pretrained-models.s3.amazonaws.com/yolox_coco/yolox_l_coco/average_model.pth",
    "yolox_t_coco": "https://deci-pretrained-models.s3.amazonaws.com/yolox_coco/yolox_tiny_coco/ckpt_best.pth",
    "yolox_n_coco": "https://deci-pretrained-models.s3.amazonaws.com/yolox_coco/yolox_n_coco/ckpt_best.pth",
    #
    "pp_lite_t_seg50_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ppliteseg/cityscapes/pplite_t_seg50/average_model.pth",
    "pp_lite_t_seg75_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ppliteseg/cityscapes/pplite_t_seg75/average_model.pth",
    "pp_lite_b_seg50_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ppliteseg/cityscapes/pplite_b_seg50/average_model.pth",
    "pp_lite_b_seg75_cityscapes": "https://deci-pretrained-models.s3.amazonaws.com/ppliteseg/cityscapes/pplite_b_seg75/average_model.pth",
    #
    "ppyoloe_s_coco": "https://deci-pretrained-models.s3.amazonaws.com/ppyolo_e/coco2017_ppyoloe_s.pth",
    "ppyoloe_m_coco": "https://deci-pretrained-models.s3.amazonaws.com/ppyolo_e/coco2017_ppyoloe_m.pth",
    "ppyoloe_l_coco": "https://deci-pretrained-models.s3.amazonaws.com/ppyolo_e/coco2017_pp_yoloe_l_best_model_21uffbb8.pth",  # 0.4948
    "ppyoloe_x_coco": "https://deci-pretrained-models.s3.amazonaws.com/ppyolo_e/coco2017_pp_yoloe_x_best_model_z03if91o.pth",  # 0.5115
}

PRETRAINED_NUM_CLASSES = {
    "imagenet": 1000,
    "imagenet21k": 21843,
    "coco_segmentation_subclass": 21,
    "cityscapes": 19,
    "coco": 80,
    "cifar10": 10,
}
