"""
* Copyright (c) 2015 Jeremy Parks. All rights reserved.
*
* Permission is hereby granted, free of charge, to any person obtaining a
* copy of this software and associated documentation files (the "Software"),
* to deal in the Software without restriction, including without limitation
* the rights to use, copy, modify, merge, publish, distribute, sublicense,
* and/or sell copies of the Software, and to permit persons to whom the
* Software is furnished to do so, subject to the following conditions:
*
* The above copyright notice and this permission notice shall be included in
* all copies or substantial portions of the Software.
*
* THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
* IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
* FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
* AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
* LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
* FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
* DEALINGS IN THE SOFTWARE.

Author: Jeremy Parks
Purpose: Create an item filter based on config files
Note: Requires Python 3.4.x
"""

desc = "Nonrare item for leveling or crafting"

# Text settings for various categories
# This is where you would define general settings for a category, such as PlayAlertSound.
# Each config should be its own array element.  Parsing will handle tabs/etc.
# ignore and hide have special meaning(see comment) everything else is local to file
settings = {
	"very high": ["SetFontSize 28",
				  "SetBackgroundColor 0 0 0 100",
				  "SetBorderColor 255 40 0"],
	"high": ["Rarity Rare",
             "SetBorderColor 255 255 119",
             "SetFontSize 34"],
	"normal": ["Rarity Rare",
             "SetBorderColor 255 255 119"],
	"low": [""],
	"ignore": [""],  # will have no styling applied and will use the default set at the end
	"hide": [""]  # Will be explicitly hidden with applied styling
}

# Base type : settings pair
# Base Type is displayed in the comments for the output file. as long as the name is unique it doesn't matter what it is
# The resulting filter is sorted by Base Type, character by character; EG "03" < "1" < "100" < "3"
# settings supports the following: 'base' (BaseType), 'class' (Class), 'other' (settings unique to that item)
#  'type' (Mandatory, indexes settings)
items = {
	"Glass Shank": {"base": "Glass Shank", "class": "Dagger", "other": ["ItemLevel <= 6"], "type": "normal"},
	"Skinning Knife": {"base": "Skinning Knife", "class": "Dagger", "other": ["ItemLevel <= 10"], "type": "normal"},
	"Carving Knife": {"base": "Carving Knife", "class": "Dagger", "other": ["ItemLevel <= 15"], "type": "normal"},
	"Stiletto": {"base": "Stiletto", "class": "Dagger", "other": ["ItemLevel <= 20"], "type": "normal"},
	"Boot Knife": {"base": "Boot Knife", "class": "Dagger", "other": ["ItemLevel <= 25"], "type": "normal"},
	"Copper Kris": {"base": "Copper Kris", "class": "Dagger", "other": ["ItemLevel <= 29"], "type": "normal"},
	"Skean": {"base": "Skean", "class": "Dagger", "other": ["ItemLevel <= 33"], "type": "normal"},
	"Imp Dagger": {"base": "Imp Dagger", "class": "Dagger", "other": ["ItemLevel <= 37"], "type": "normal"},
	"Flaying Knife": {"base": "Flaying Knife", "class": "Dagger", "other": ["ItemLevel <= 40"], "type": "normal"},
	"Prong Dagger": {"base": "Prong Dagger", "class": "Dagger", "other": ["ItemLevel <= 41"], "type": "normal"},
	"Butcher Knife": {"base": "Butcher Knife", "class": "Dagger", "other": ["ItemLevel <= 43"], "type": "normal"},
	"Poignard": {"base": "Poignard", "class": "Dagger", "other": ["ItemLevel <= 46"], "type": "normal"},
	"Boot Blade": {"base": "Boot Blade", "class": "Dagger", "other": ["ItemLevel <= 49"], "type": "normal"},
	"Golden Kris": {"base": "Golden Kris", "class": "Dagger", "other": ["ItemLevel <= 52"], "type": "normal"},
	"Royal Skean": {"base": "Royal Skean", "class": "Dagger", "other": ["ItemLevel <= 55"], "type": "normal"},
	"Fiend Dagger": {"base": "Fiend Dagger", "class": "Dagger", "other": ["ItemLevel <= 58"], "type": "normal"},
	"Trisula": {"base": "Trisula", "class": "Dagger", "other": ["ItemLevel <= 60"], "type": "normal"},
	"Gutting Knife": {"base": "Gutting Knife", "class": "Dagger", "other": ["ItemLevel <= 61"], "type": "normal"},
	"Slaughter Knife": {"base": "Slaughter Knife", "class": "Dagger", "other": ["ItemLevel <= 63"], "type": "normal"},
	"Ambusher": {"base": "Ambusher", "class": "Dagger", "other": ["ItemLevel <= 65"], "type": "normal"},
	"Ezomyte Dagger": {"base": "Ezomyte Dagger", "class": "Dagger", "other": ["ItemLevel <= 67"], "type": "normal"},
	"Platinum Kris": {"base": "Platinum Kris", "class": "Dagger", "other": ["ItemLevel <= 69"], "type": "normal"},
	"Imperial Skean": {"base": "Imperial Skean", "class": "Dagger", "other": ["ItemLevel <= 71"], "type": "normal"},
	"Demon Dagger": {"base": "Demon Dagger", "class": "Dagger", "other": ["ItemLevel <= 73"], "type": "normal"},
	"Sai": {"base": "Sai", "class": "Dagger", "other": ["ItemLevel <= 75"], "type": "normal"}
}