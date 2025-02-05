# -*- coding: utf-8 -*-
uiGuideBookPath = "arrisFarmersDelightScripts.modClient.uiScript.uiGuideBook.guideBook"
uiGuideBookScreen = "guideBook.main"

# 可以烹饪的食物及输出结果字典
CanCookedFoodDict = {
    "minecraft:beef": "minecraft:cooked_beef",
    "minecraft:chicken": "minecraft:cooked_chicken",
    "minecraft:cod": "minecraft:cooked_cod",
    "minecraft:mutton": "minecraft:cooked_mutton",
    "minecraft:porkchop": "minecraft:cooked_porkchop",
    "minecraft:potato": "minecraft:baked_potato",
    "minecraft:rabbit": "minecraft:cooked_rabbit",
    "minecraft:salmon": "minecraft:cooked_salmon",
    "minecraft:egg": "arris:fried_egg",
    "arris:cod_slice": "arris:cooked_cod_slice",
    "arris:salmon_slice": "arris:cooked_salmon_slice",
    "arris:chicken_cuts": "arris:cooked_chicken_cuts",
    "arris:minced_beef": "arris:beef_patty",
    "arris:bacon": "arris:cooked_bacon",
    "arris:mutton_chops": "arris:cooked_mutton_chops"
}
# 可以提供火源的方块列表
CanProvideHeatBlockList = [
    "minecraft:fire",
    "minecraft:soul_fire",
    "minecraft:campfire",
    "minecraft:soul_campfire",
    "minecraft:lava",
    "minecraft:flowing_lava",
    "minecraft:magma",
    "arris:stove"
]
# 刀列表
knifeList = [
    "arris:flint_knife",
    "arris:golden_knife",
    "arris:iron_knife",
    "arris:diamond_knife",
    "arris:netherite_knife",
    "ends_delight:end_stone_knife",
    "ends_delight:purpur_knife",
    "ends_delight:dragon_egg_shell_knife",
    "ends_delight:dragon_tooth_knife"
]
# 斧头列表
axeList = [
    "minecraft:wooden_axe",
    "minecraft:stone_axe",
    "minecraft:iron_axe",
    "minecraft:golden_axe",
    "minecraft:diamond_axe",
    "minecraft:netherite_axe"
]
# 可以在砧板上切的食物及输出字典和使用工具
CuttingBoardDict = {
    ("minecraft:beef", 0): {"itemList": [{"itemName": "arris:minced_beef", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_beef", 0): {"itemList": [{"itemName": "arris:beef_patty", "count": 2}], "tool": knifeList},
    ("minecraft:chicken", 0): {"itemList": [{"itemName": "arris:chicken_cuts", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_chicken", 0): {"itemList": [{"itemName": "arris:cooked_chicken_cuts", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:porkchop", 0): {"itemList": [{"itemName": "arris:bacon", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_porkchop", 0): {"itemList": [{"itemName": "arris:cooked_bacon", "count": 2}], "tool": knifeList},
    ("minecraft:mutton", 0): {"itemList": [{"itemName": "arris:mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:muttonraw", 0): {"itemList": [{"itemName": "arris:mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:cooked_mutton", 0): {"itemList": [{"itemName": "arris:cooked_mutton_chops", "count": 2}], "tool": knifeList},
    ("minecraft:cod", 0): {"itemList": [{"itemName": "arris:cod_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_cod", 0): {"itemList": [{"itemName": "arris:cooked_cod_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:salmon", 0): {"itemList": [{"itemName": "arris:salmon_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:cooked_salmon", 0): {"itemList": [{"itemName": "arris:cooked_salmon_slice", "count": 2}, {"itemName": "minecraft:bone_meal", "count": 1}], "tool": knifeList},
    ("minecraft:pumpkin", 0): {"itemList": [{"itemName": "arris:pumpkin_slice", "count": 4}], "tool": knifeList},
    ("minecraft:cake", 0): {"itemList": [{"itemName": "arris:cake_slice", "count": 7}], "tool": knifeList},
    ("arris:ham", 0): {"itemList": [{"itemName": "minecraft:porkchop", "count": 2}, {"itemName": "minecraft:bone", "count": 1}], "tool": knifeList},
    ("arris:smoked_ham", 0): {"itemList": [{"itemName": "minecraft:cooked_porkchop", "count": 2}, {"itemName": "minecraft:bone", "count": 1}], "tool": knifeList},
    ("arris:cabbage", 0): {"itemList": [{"itemName": "arris:cabbage_leaf", "count": 2}], "tool": knifeList},
    ("arris:wheat_dough", 0): {"itemList": [{"itemName": "arris:raw_pasta", "count": 1}], "tool": knifeList},
    ("arris:apple_pie_item", 0): {"itemList": [{"itemName": "arris:apple_pie_slice", "count": 4}], "tool": knifeList},
    ("arris:chocolate_pie_item", 0): {"itemList": [{"itemName": "arris:chocolate_pie_slice", "count": 4}], "tool": knifeList},
    ("arris:kelp_roll", 0): {"itemList": [{"itemName": "arris:kelp_roll_slice", "count": 3}], "tool": knifeList},
    ("arris:sweet_berry_cheesecake_item", 0): {"itemList": [{"itemName": "arris:sweet_berry_cheesecake_slice", "count": 4}], "tool": knifeList},
    ("arris:rice_panicle", 0): {"itemList": [{"itemName": "arris:rice", "count": 1}, {"itemName": "arris:straw", "count": 1}], "tool": knifeList},
    ("minecraft:oak_log", 0): {"itemList": [{"itemName": "minecraft:stripped_oak_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:spruce_log", 0): {"itemList": [{"itemName": "minecraft:stripped_spruce_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:acacia_log", 0): {"itemList": [{"itemName": "minecraft:stripped_acacia_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:birch_log", 0): {"itemList": [{"itemName": "minecraft:stripped_birch_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:cherry_log", 0): {"itemList": [{"itemName": "minecraft:stripped_cherry_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:dark_oak_log", 0): {"itemList": [{"itemName": "minecraft:stripped_dark_oak_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:jungle_log", 0): {"itemList": [{"itemName": "minecraft:stripped_jungle_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:mangrove_log", 0): {"itemList": [{"itemName": "minecraft:stripped_mangrove_log", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:crimson_stem", 0): {"itemList": [{"itemName": "minecraft:stripped_crimson_stem", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:crimson_hyphae", 0): {"itemList": [{"itemName": "minecraft:stripped_crimson_hyphae", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:warped_stem", 0): {"itemList": [{"itemName": "minecraft:stripped_warped_stem", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList},
    ("minecraft:warped_hyphae", 0): {"itemList": [{"itemName": "minecraft:stripped_warped_hyphae", "count": 1}, {"itemName": "arris:tree_bark", "count": 1}], "tool": axeList}
}
# 可堆肥的物品
ComposterItemDict = {
    ("arris:cabbage_seeds", 0): 50,
    ("arris:tomato_seeds", 0): 50,
    ("arris:rotten_tomato", 0): 40,
    ("arris:cabbage_leaf", 0): 50,
    ("arris:rice", 0): 50,
    ("arris:tree_bark", 0): 50,
    ("arris:straw", 0): 50,
    ("arris:cabbage", 0): 70,
    ("arris:rice_panicle", 0): 60,
    ("arris:tomato", 0): 70,
    ("arris:onion", 0): 70
}
# 炉灶列表
StoveList = [
    "arris:stove"
]
# 物品转变为方块字典
itemChangeBlockDict = {
    "arris:skillet_item": "arris:skillet",
    "arris:apple_pie_item": "arris:apple_pie",
    "arris:sweet_berry_cheesecake_item": "arris:sweet_berry_cheesecake",
    "arris:chocolate_pie_item": "arris:chocolate_pie",
}
# 派列表
pieList = [
    "arris:apple_pie",
    "arris:sweet_berry_cheesecake",
    "arris:chocolate_pie"
]
# 可攀爬的方块列表
canClimbList = [
    "arris:rope",
    "arris:tomatoes_vine_stage0",
    "arris:tomatoes_vine_stage1",
    "arris:tomatoes_vine_stage2",
    "arris:tomatoes_vine_stage3"
]
# 橱柜列表
cabinetList = [
    "arris:oak_cabinet",
    "arris:spruce_cabinet",
    "arris:birch_cabinet",
    "arris:jungle_cabinet",
    "arris:acacia_cabinet",
    "arris:dark_oak_cabinet",
    "arris:mangrove_cabinet",
    "arris:cherry_cabinet",
    "arris:bamboo_cabinet",
    "arris:crimson_cabinet",
    "arris:warped_cabinet"
]
# 野生作物方块且允许种植在其方块上的列表字典
WildCropDict = {
    "arris:sandy_shrub": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_beetroots": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_carrots": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_cabbages": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_onions": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_rice": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_tomatoes": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"],
    "arris:wild_potatoes": ["minecraft:sand", "minecraft:grass", "minecraft:dirt", "minecraft:dirt_with_roots", "minecraft:farmland", "minecraft:podzol", "minecraft:mycelium", "minecraft:mud"]
}
# 原版所有负面效果
negativeEffect = [
    "slowness",
    "mining_fatigue",
    "instant_damage",
    "nausea",
    "blindness",
    "hunger",
    "weakness",
    "wither",
    "poison",
    "fatal_poison"
    "wither",
    "levitation",
    "darkness",
    "wind_charged",
    "weaving",
    "oozing",
    "infested"
]
# 盘装食物
platePackagedFoodDict = {
    "arris:roast_chicken_block_stage0": {"target": "arris:roast_chicken_block_stage1", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage1": {"target": "arris:roast_chicken_block_stage2", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage2": {"target": "arris:roast_chicken_block_stage3", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_stage3": {"target": "arris:roast_chicken_block_leftover", "item": "arris:roast_chicken"},
    "arris:roast_chicken_block_leftover": {"target": None, "item": None},
    "arris:stuffed_pumpkin_block_stage0": {"target": "arris:stuffed_pumpkin_block_stage1", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage1": {"target": "arris:stuffed_pumpkin_block_stage2", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage2": {"target": "arris:stuffed_pumpkin_block_stage3", "item": "arris:stuffed_pumpkin"},
    "arris:stuffed_pumpkin_block_stage3": {"target": None, "item": None},
    "arris:honey_glazed_ham_block_stage0": {"target": "arris:honey_glazed_ham_block_stage1", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage1": {"target": "arris:honey_glazed_ham_block_stage2", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage2": {"target": "arris:honey_glazed_ham_block_stage3", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_stage3": {"target": "arris:honey_glazed_ham_block_leftover", "item": "arris:honey_glazed_ham"},
    "arris:honey_glazed_ham_block_leftover": {"target": None, "item": None},
    "arris:shepherds_pie_block_stage0": {"target": "arris:shepherds_pie_block_stage1", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage1": {"target": "arris:shepherds_pie_block_stage2", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage2": {"target": "arris:shepherds_pie_block_stage3", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_stage3": {"target": "arris:shepherds_pie_block_leftover", "item": "arris:shepherds_pie"},
    "arris:shepherds_pie_block_leftover": {"target": None, "item": None},
    "arris:rice_roll_medley_block_stage0": {"target": "arris:rice_roll_medley_block_stage1", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage1": {"target": "arris:rice_roll_medley_block_stage2", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage2": {"target": "arris:rice_roll_medley_block_stage3", "item": "arris:kelp_roll_slice"},
    "arris:rice_roll_medley_block_stage3": {"target": "arris:rice_roll_medley_block_stage4", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage4": {"target": "arris:rice_roll_medley_block_stage5", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage5": {"target": "arris:rice_roll_medley_block_stage6", "item": "arris:salmon_roll"},
    "arris:rice_roll_medley_block_stage6": {"target": "arris:rice_roll_medley_block_stage7", "item": "arris:cod_roll"},
    "arris:rice_roll_medley_block_stage7": {"target": "arris:rice_roll_medley_block_leftover", "item": "arris:cod_roll"},
    "arris:rice_roll_medley_block_leftover": {"target": None, "item": None},
}
# 农作物下一阶段字典
cropsDict = {
    "arris:cabbages_stage0": "arris:cabbages_stage1",
    "arris:cabbages_stage1": "arris:cabbages_stage2",
    "arris:cabbages_stage2": "arris:cabbages_stage3",
    "arris:cabbages_stage3": "arris:cabbages_stage4",
    "arris:cabbages_stage4": "arris:cabbages_stage5",
    "arris:cabbages_stage5": "arris:cabbages_stage6",
    "arris:cabbages_stage6": "arris:cabbages_stage7",
    "arris:cabbages_stage7": "",
    "arris:budding_tomatoes_stage0": "arris:budding_tomatoes_stage1",
    "arris:budding_tomatoes_stage1": "arris:budding_tomatoes_stage2",
    "arris:budding_tomatoes_stage2": "arris:budding_tomatoes_stage3",
    "arris:budding_tomatoes_stage3": "arris:budding_tomatoes_stage4",
    "arris:budding_tomatoes_stage4": "arris:budding_tomatoes_stage5",
    "arris:budding_tomatoes_stage5": "arris:budding_tomatoes_stage6",
    "arris:budding_tomatoes_stage6": "",
    "arris:tomatoes_vine_stage0": "arris:tomatoes_vine_stage1",
    "arris:tomatoes_vine_stage1": "arris:tomatoes_vine_stage2",
    "arris:tomatoes_vine_stage2": "arris:tomatoes_vine_stage3",
    "arris:tomatoes_vine_stage3": "",
    "arris:onions_stage0": "arris:onions_stage1",
    "arris:onions_stage1": "arris:onions_stage2",
    "arris:onions_stage2": "arris:onions_stage3",
    "arris:onions_stage3": "",
    "arris:organic_compost_stage0": "arris:organic_compost_stage1",
    "arris:organic_compost_stage1": "arris:organic_compost_stage2",
    "arris:organic_compost_stage2": "arris:organic_compost_stage3",
    "arris:organic_compost_stage3": "arris:rich_soil",
    "arris:rich_soil": "",
    "arris:rich_soil_wheat0": "arris:rich_soil_wheat1",
    "arris:rich_soil_wheat1": "arris:rich_soil_wheat2",
    "arris:rich_soil_wheat2": "arris:rich_soil_wheat3",
    "arris:rich_soil_wheat3": "arris:rich_soil_wheat4",
    "arris:rich_soil_wheat4": "arris:rich_soil_wheat5",
    "arris:rich_soil_wheat5": "arris:rich_soil_wheat6",
    "arris:rich_soil_wheat6": "arris:rich_soil_wheat7",
    "arris:rich_soil_wheat7": "",
    "arris:rich_soil_beetroot0": "arris:rich_soil_beetroot1",
    "arris:rich_soil_beetroot1": "arris:rich_soil_beetroot2",
    "arris:rich_soil_beetroot2": "arris:rich_soil_beetroot3",
    "arris:rich_soil_beetroot3": "",
    "arris:rich_soil_carrots0": "arris:rich_soil_carrots1",
    "arris:rich_soil_carrots1": "arris:rich_soil_carrots2",
    "arris:rich_soil_carrots2": "arris:rich_soil_carrots3",
    "arris:rich_soil_carrots3": "",
    "arris:rich_soil_potatoes0": "arris:rich_soil_potatoes1",
    "arris:rich_soil_potatoes1": "arris:rich_soil_potatoes2",
    "arris:rich_soil_potatoes2": "arris:rich_soil_potatoes3",
    "arris:rich_soil_potatoes3": "",
    "arris:rice_stage0": "arris:rice_stage1",
    "arris:rice_stage1": "arris:rice_stage2",
    "arris:rice_stage2": "arris:rice_stage3",
    "arris:rice_stage3": "",
    "arris:rice_upper_crop_stage0": "arris:rice_upper_crop_stage1",
    "arris:rice_upper_crop_stage1": "arris:rice_upper_crop_stage2",
    "arris:rice_upper_crop_stage2": "arris:rice_upper_crop_stage3",
    "arris:rice_upper_crop_stage3": "",
}
# 厨锅配方
CookingPotRecipeList = [
    {
        "Recipe": [
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0)
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0)
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:brown_mushroom", 0)
            ]
        ],
        "CookResult": ("minecraft:mushroom_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蘑菇煲"
    },
    {
        "Recipe": [
            [
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0)
            ]
        ],
        "CookResult": ("minecraft:beetroot_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "甜菜汤"
    },
    {
        "Recipe": [
            [
                ("minecraft:rabbit", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:carrot", 0)
            ],
            [
                ("minecraft:rabbit", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:carrot", 0)
            ]
        ],
        "CookResult": ("minecraft:rabbit_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "兔肉煲"
    },
    {
        "Recipe": [
            [
                ("arris:tomato", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:tomato_sauce", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "番茄酱"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0)
            ]
        ],
        "CookResult": ("arris:cooked_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "米饭"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0),
                ("minecraft:egg", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ]
        ],
        "CookResult": ("arris:fried_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "炒饭"
    },
    {
        "Recipe": [
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:bacon", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:minced_beef", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:cod_slice", 0)
            ],
            [
                ("arris:wheat_dough", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:onion", 0),
                ("arris:salmon_slice", 0)
            ]
        ],
        "CookResult": ("arris:dumplings", 0),
        "Vessel": ("arris:cabbage_leaf", 0),
        "PushItem": [
        ],
        "text": "饺子"
    },
    {
        "Recipe": [
            [
                ("arris:minced_beef", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:pasta_with_meatballs", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "肉丸意面"
    },
    {
        "Recipe": [
            [
                ("arris:mutton_chops", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:pasta_with_mutton_chop", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "羊排意面"
    },
    {
        "Recipe": [
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("minecraft:brown_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("minecraft:red_mushroom", 0),
                ("arris:rice", 0),
                ("minecraft:carrot", 0),
            ]
        ],
        "CookResult": ("arris:mushroom_rice", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蘑菇饭"
    },
    {
        "Recipe": [
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:carrot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0),
            ],
            [
                ("minecraft:brown_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0),
            ],
            [
                ("minecraft:red_mushroom", 0),
                ("arris:raw_pasta", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0),
            ]
        ],
        "CookResult": ("arris:vegetable_noodles", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜面"
    },
    {
        "Recipe": [
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:carrot", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:beetroot", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:tomato", 0),
                ("arris:onion", 0),
                ("minecraft:beetroot", 0),
                ("arris:tomato", 0)
            ]
        ],
        "CookResult": ("arris:ratatouille", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜杂烩"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0),
                ("minecraft:ink_sac", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:raw_pasta", 0),
                ("arris:tomato", 0),
                ("minecraft:ink_sac", 0)
            ]
        ],
        "CookResult": ("arris:squid_ink_pasta", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鱿鱼墨面"
    },
    {
        "Recipe": [
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:glow_berries", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:glow_berries", 0),
                ("minecraft:beetroot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:brown_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("arris:onion", 0),
                ("arris:tomato", 0)
            ],
            [
                ("arris:rice", 0),
                ("minecraft:red_mushroom", 0),
                ("minecraft:potato", 0),
                ("minecraft:sweet_berries", 0),
                ("arris:onion", 0),
                ("arris:tomato", 0)
            ],
        ],
        "CookResult": ("arris:stuffed_pumpkin_block_stage0", 0),
        "Vessel": ("minecraft:pumpkin", 0),
        "PushItem": [
        ],
        "text": "填馅南瓜"
    },
    {
        "Recipe": [
            [
                ("arris:bacon", 0),
                ("arris:bacon", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:minced_beef", 0),
                ("arris:minced_beef", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:mutton_chops", 0),
                ("arris:mutton_chops", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:cod_slice", 0),
                ("arris:cod_slice", 0),
                ("arris:cabbage_leaf", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:salmon_slice", 0),
                ("arris:cabbage_leaf", 0)
            ]
        ],
        "CookResult": ("arris:cabbage_rolls", 0),
        "Vessel": ("arris:cabbage_leaf", 0),
        "PushItem": [
        ],
        "text": "卷心菜卷"
    },
    {
        "Recipe": [
            [
                ("minecraft:bone", 0),
                ("minecraft:brown_mushroom", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:red_mushroom", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:sweet_berries", 0)
            ],
            [
                ("minecraft:bone", 0),
                ("minecraft:glow_berries", 0)
            ]
        ],
        "CookResult": ("arris:bone_broth", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "大骨汤"
    },
    {
        "Recipe": [
            [
                ("arris:minced_beef", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:cookbeef_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "牛肉炖"
    },
    {
        "Recipe": [
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("minecraft:beetroot", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:tomato", 0)
            ],
            [
                ("arris:chicken_cuts", 0),
                ("arris:cabbage_leaf", 0),
                ("minecraft:carrot", 0),
                ("arris:pumpkin_slice", 0)
            ]
        ],
        "CookResult": ("arris:chicken_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鸡肉汤"
    },
    {
        "Recipe": [
            [
                ("arris:cabbage_leaf", 0),
                ("minecraft:beetroot", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:cabbage_leaf", 0),
                ("arris:pumpkin_slice", 0),
                ("minecraft:carrot", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:vegetable_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "蔬菜汤"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("arris:tomato", 0),
                ("arris:onion", 0)
            ],
            [
                ("arris:salmon_slice", 0),
                ("arris:tomato", 0),
                ("arris:onion", 0)
            ]
        ],
        "CookResult": ("arris:fish_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "鱼肉炖"
    },
    {
        "Recipe": [
            [
                ("arris:pumpkin_slice", 0),
                ("arris:cabbage_leaf", 0),
                ("arris:bacon", 0),
                ("arris:milk_bottle", 0)
            ]
        ],
        "CookResult": ("arris:pumpkin_soup", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "南瓜汤"
    },
    {
        "Recipe": [
            [
                ("arris:cod_slice", 0),
                ("minecraft:egg", 0),
                ("arris:tomato", 0),
                ("minecraft:potato", 0)
            ],
            [
                ("arris:cod_slice", 0),
                ("minecraft:egg", 0),
                ("arris:pumpkin_slice", 0),
                ("minecraft:potato", 0)
            ]
        ],
        "CookResult": ("arris:baked_cod_stew", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "烘焙鳕鱼炖"
    },
    {
        "Recipe": [
            [
                ("arris:milk_bottle", 0),
                ("minecraft:cocoa_beans", 0),
                ("minecraft:cocoa_beans", 0),
                ("minecraft:sugar", 0)
            ]
        ],
        "CookResult": ("arris:hot_cocoa", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "热可可"
    },
    {
        "Recipe": [
            [
                ("minecraft:apple", 0),
                ("minecraft:apple", 0),
                ("minecraft:sugar", 0)
            ]
        ],
        "CookResult": ("arris:apple_cider", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
        ],
        "text": "苹果酒"
    },
    {
        "Recipe": [
            [
                ("minecraft:glow_berries", 0),
                ("minecraft:egg", 0),
                ("minecraft:sugar", 0),
                ("arris:milk_bottle", 0)
            ]
        ],
        "CookResult": ("arris:glow_berry_custard", 0),
        "Vessel": ("minecraft:glass_bottle", 0),
        "PushItem": [
            ("minecraft:glass_bottle", 0)
        ],
        "text": "发光浆果蛋奶沙司"
    },
    {
        "Recipe": [
            [
                ("minecraft:rotten_flesh", 0),
                ("minecraft:bone_meal", 0),
                ("arris:rice", 0),
                ("minecraft:chicken", 0)
            ]
        ],
        "CookResult": ("arris:dog_food", 0),
        "Vessel": ("minecraft:bowl", 0),
        "PushItem": [
        ],
        "text": "狗粮"
    }
]

def ArrisFarmersDelightInterface(target, element=None):
    """
    向配置字典或列表内添加元素
    :param target: 需要调用的变量名称 (str)
    :param element: 需要添加进去的元素(如果目标是list,则支持str或list,如果目标是dict,则仅支持dict)
    :return 修改结果
    """
    globalVar = globals()
    if not target:
        return False
    if not globalVar[target]:
        return False
    if target == "CookingPotRecipeList":
        for recipe in element["Recipe"]:
            if len(recipe) > 6:
                return False

    targetType = type(globalVar[target]).__name__
    elementType = type(element).__name__
    if targetType == "list":
        if elementType != "list":
            globalVar[target].append(element)
        else:
            globalVar[target] += element
    elif targetType == "dict" and elementType == "dict":
        globalVar[target].update(element)
    return globalVar[target]

def ArrisFarmersDelightObtain(target):
    """
    获取配置字典或列表
    :param target: 需要获取的变量名称 (str)
    :return 结果
    """
    globalVar = globals()
    if not target:
        return False
    if not globalVar[target]:
        return False
    else:
        return globalVar[target]

def AddCookingPotRecipe(name, recipe):
    """
    在厨锅原有的配方上，新增额外配方
    :param name: 对应食物id (str)
    :param recipe: 对应需要添加上去的配方 (list)
    :return 结果
    """
    if not name:
        return False
    if len(recipe) > 6:
        return False
    for recipeDict in CookingPotRecipeList:
        if recipeDict["CookResult"][0] == name:
            recipeDict["Recipe"].append(recipe)
            return recipeDict["Recipe"]
        else:
            return False
