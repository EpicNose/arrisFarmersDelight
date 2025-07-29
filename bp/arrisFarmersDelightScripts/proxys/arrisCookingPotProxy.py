# -*- coding: utf-8 -*-
from ..QingYunModLibs.ClientMod import *
from ..QingYunModLibs.SystemApi import *

CustomUIScreenProxy = clientApi.GetUIScreenProxyCls()
playerId = clientApi.GetLocalPlayerId()
levelId = clientApi.GetLevelId()
ViewBinder = clientApi.GetViewBinderCls()

uiRootPanelPath = "variables_button_mappings_and_controls/safezone_screen_matrix/inner_matrix/safezone_screen_panel/root_screen_panel"
cookRecipePanel = uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/cookbook_bg/stack_panel"
cookingPotFireIcon = uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/bg/arris_cooking_pot_top_half/cooking_pot/heat/fire"

class arrisCookingPotProxy(CustomUIScreenProxy):
    def __init__(self, screenName, screenNode):
        CustomUIScreenProxy.__init__(self, screenName, screenNode)
        self.screenNode = screenNode
        self.cookingPotRecipeList = ClientComp.CreateModAttr(playerId).GetAttr("arrisCookingPotRecipeList")
        self.foodRecipe = None # 配方面板UI实例
        self.foodRecipeList = None # 选择的食谱列表
        self.foodRecipeIndex = 0 # 选择的食谱索引
        self.RecipeList = self.cookingPotRecipeList
        self.foodRecipeTimer = None
        self.foodRecipeSearchDict = None
        self.allItemList = ClientComp.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)

    def OnCreate(self):
        self.foodRecipe = self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/option_bg/stack_panel/scroll_panel/scroll_view").asScrollView().GetScrollViewContentControl()
        CreateTimer(0.1, self.CookingPotInit, False)

    def OnTick(self):
        self.allItemList = ClientComp.CreateItem(playerId).GetPlayerAllItems(clientApi.GetMinecraftEnum().ItemPosType.INVENTORY, True)
        pos = ClientComp.CreateModAttr(playerId).GetAttr("arrisUsedCookingPotPos")
        if not pos:
            return
        blockEntityData = ClientComp.CreateBlockInfo(levelId).GetBlockEntityData(pos)
        if not blockEntityData:
            return
        heatEnable = blockEntityData["exData"]["heatEnable"]["__value__"]
        if not heatEnable:
            self.screenNode.GetBaseUIControl(cookingPotFireIcon).SetVisible(False)
        else:
            self.screenNode.GetBaseUIControl(cookingPotFireIcon).SetVisible(True)

        previewItemSlot = blockEntityData["exData"]["previewItemSlot"][0]
        if previewItemSlot and previewItemSlot != {'__type__': 1, '__value__': 1}:
            itemDict = {
                "newItemName": previewItemSlot.get("newItemName").get("__value__"),
                "newAuxValue": previewItemSlot.get("newAuxValue").get("__value__"),
                "count": previewItemSlot.get("count").get("__value__")
            }
        else:
            itemDict = {}
        self.SetPreviewItemSlot(itemDict)
        timer = blockEntityData["exData"]["timer"]
        arrowControl = self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/bg/arris_cooking_pot_top_half/cooking_pot/arrow")
        if timer and arrowControl:
            progress = arrowControl.GetChildByName("progress")
            progress.asImage().SetSpriteClipRatio(timer["__value__"] / 10.0)

    @ViewBinder.binding(ViewBinder.BF_EditFinished, "#arrisCookingPotEditBox")
    def EditBoxFinished(self, args):
        text = args["Text"]
        recipeList = []
        for index in range(0, len(self.cookingPotRecipeList)):
            recipeDict = self.cookingPotRecipeList[index]
            recipeText = recipeDict["text"]
            if text in recipeText:
                recipeList.append(recipeDict)
        self.RecipeList = recipeList
        self.screenNode.UpdateScreen(True)

    def FoodRecipeTimerSwitch(self):
        if self.foodRecipeList:
            self.foodRecipeIndex += 1
            if self.foodRecipeIndex >= len(self.foodRecipeList):
                self.foodRecipeIndex = 0
            recipe = self.foodRecipeList[self.foodRecipeIndex]
            for index in range(0, len(recipe)):
                recipeItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1))
                itemRenderer = recipeItem.GetChildByName("item_renderer")
                itemRenderer.SetVisible(True)
                result = itemRenderer.asItemRenderer().SetUiItem(recipe[index][0], recipe[index][1])
                if result is False:
                    itemRenderer.asItemRenderer().SetUiItem("minecraft:barrier", 0)
            for i in range(len(recipe), 6):
                recipeItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(i + 1))
                itemRenderer = recipeItem.GetChildByName("item_renderer")
                itemRenderer.SetVisible(False)

    def SetPreviewItemSlot(self, itemDict):
        previewControl = self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/bg/arris_cooking_pot_top_half/cooking_pot/preview/item")
        if not itemDict:
            previewControl.GetChildByName("item_renderer").SetVisible(False)
            previewControl.GetChildByName("stack_count_label").asLabel().SetText("")
            return
        itemName = itemDict["newItemName"]
        auxValue = itemDict["newAuxValue"]
        count = itemDict["count"]
        itemRenderer = previewControl.GetChildByName("item_renderer").asItemRenderer()
        countLabel = previewControl.GetChildByName("stack_count_label").asLabel()
        if count == 1:
            count = ""
        countLabel.SetText(str(count))
        itemRenderer.SetVisible(True)
        itemRenderer.SetUiItem(itemName, auxValue, False, itemDict.get("userData", {}))

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, "#arrisCookingPotAddFood")
    def CookingPotAddFood(self, args):
        flag = False
        indexList = []
        allItemList = []
        for i in range(0, len(self.allItemList)):
            itemDict = self.allItemList[i]
            if not itemDict:
                allItemList.append(None)
                continue
            allItemList.append((itemDict["newItemName"], itemDict["newAuxValue"]))
        for recipe in self.foodRecipeList:
            for recipeItem in recipe:
                inputSlot = (recipeItem[0], recipeItem[1])
                if inputSlot in allItemList:
                    indexList.append(allItemList.index(inputSlot))
            if len(indexList) != len(recipe):
                indexList = []
            else:
                flag = True
            if flag is True:
                if len(indexList) != len(recipe):
                    return
                break
        inputList = [index for index in range(len(indexList))]
        if not inputList:
            return
        dimensionId = ClientComp.CreateGame(playerId).GetCurrentDimension()
        pos = ClientComp.CreateModAttr(playerId).GetAttr("arrisUsedCookingPotPos")
        data = {"playerId": playerId, "blockPos": pos, "dimensionId": dimensionId, "inputList": inputList, "indexList": indexList}
        CallServer("CookingPotAddFood", data)

    @ViewBinder.binding_collection(ViewBinder.BF_BindInt, "food_recipe_book", "#recipe_book_total_items")
    def FoodRecipeBook(self, args):
        return len(self.RecipeList)

    @ViewBinder.binding_collection(ViewBinder.BF_BindBool, "food_recipe_book", "#arrisfoodRecipe.visible")
    def SetFoodRecipeItemVisible(self, index):
        if index >= len(self.RecipeList):
            return False
        recipeDict = self.RecipeList[index]
        cookResult = recipeDict["CookResult"]
        itemRenderer = self.foodRecipe.GetChildByPath("/foodRecipe{}/item_renderer".format(index + 1))
        if not itemRenderer:
            return False
        result = itemRenderer.asItemRenderer().SetUiItem(cookResult[0], cookResult[1])
        if result is False:
            itemRenderer.asItemRenderer().SetUiItem("minecraft:barrier", 0)
        return True

    @ViewBinder.binding(ViewBinder.BF_ButtonClickUp, "#arrisCookingPotRecipeButtonClick")
    def ClickRecipeButton(self, args):
        index = args["#collection_index"]
        if index >= len(self.RecipeList):
            return
        recipeDict = self.RecipeList[index]
        recipeList = recipeDict["Recipe"]
        recipeText = recipeDict["text"]
        self.foodRecipeList = recipeList
        self.foodRecipeIndex = 0
        self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/cookbook_bg/stack_panel/button_panel/add_food").SetVisible(True)
        if self.foodRecipeTimer:
            DestroyTimer(self.foodRecipeTimer)
        self.foodRecipeTimer = CreateTimer(1.0, self.FoodRecipeTimerSwitch, True)

        recipe = self.foodRecipeList[self.foodRecipeIndex]
        for index in range(0, 6):
            recipeItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1)).GetChildByName("item_renderer")
            recipeItem.SetVisible(False)
        for index in range(0, len(recipe)):
            recipeItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1))
            itemRenderer = recipeItem.GetChildByName("item_renderer")
            itemRenderer.SetVisible(True)
            result = itemRenderer.asItemRenderer().SetUiItem(recipe[index][0], recipe[index][1])
            if result is False:
                itemRenderer.asItemRenderer().SetUiItem("minecraft:barrier", 0)

        previewItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/preview/item/item_renderer")
        result = previewItem.asItemRenderer().SetUiItem(recipeDict["CookResult"][0], recipeDict["CookResult"][1])
        if result is False:
            previewItem.asItemRenderer().SetUiItem("minecraft:barrier", 0)
        previewItem.SetVisible(True)
        vesselItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/vessel/item_renderer")
        if recipeDict.get("Vessel"):
            vesselItem.asItemRenderer().SetUiItem(recipeDict["Vessel"][0], recipeDict["Vessel"][1])
            vesselItem.SetVisible(True)
        else:
            vesselItem.SetVisible(False)
        self.screenNode.GetBaseUIControl(cookRecipePanel + "/food_title/title").asLabel().SetText(recipeText)

    def CookingPotInit(self):
        vessel = self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/bg/arris_cooking_pot_top_half/cooking_pot/cookingpotContainerGrid/cookingpot_grid_item7")
        vessel.SetPosition((75, 38))
        result = self.screenNode.GetBaseUIControl(uiRootPanelPath + "/root_panel/common_panel/bg_image/cookpot_panel/bg/arris_cooking_pot_top_half/cooking_pot/cookingpotContainerGrid/cookingpot_grid_item8")
        result.SetPosition((108, 38))

        previewItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/preview/item/item_renderer")
        previewItem.SetVisible(False)
        vesselItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/vessel/item_renderer")
        vesselItem.SetVisible(False)
        self.screenNode.GetBaseUIControl(cookRecipePanel + "/food_title/title").asLabel().SetText("请选择食谱")
        for index in xrange(6):
            recipeItem = self.screenNode.GetBaseUIControl(cookRecipePanel + "/cook_recipe/grid/recipeItem{}".format(index + 1))
            itemRenderer = recipeItem.GetChildByName("item_renderer")
            itemRenderer.SetVisible(False)

        self.screenNode.UpdateScreen(True)

    def OnDestroy(self):
        if self.foodRecipeTimer:
            DestroyTimer(self.foodRecipeTimer)
