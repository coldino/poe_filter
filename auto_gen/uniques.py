#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/21/2018(m/d/y) 07:25:12 UTC from "Standard" data

desc = "Unique"

# Base type : settings pair
items = {
	"0 Ambush Mitts": {"base": "Ambush Mitts", "type": "unique extremely high"},
	"0 Blood Sceptre": {"base": "Blood Sceptre", "type": "unique extremely high"},
	"0 Callous Mask": {"base": "Callous Mask", "type": "unique extremely high"},
	"0 Carnal Boots": {"base": "Carnal Boots", "type": "unique extremely high"},
	"0 Chateau Map": {"base": "Chateau Map", "type": "unique extremely high"},
	"0 Crusader Boots": {"base": "Crusader Boots", "type": "unique extremely high"},
	"0 Ezomyte Tower Shield": {"base": "Ezomyte Tower Shield", "type": "unique extremely high"},
	"0 Golden Hoop": {"base": "Golden Hoop", "type": "unique extremely high"},
	"0 Golden Mantle": {"base": "Golden Mantle", "type": "unique extremely high"},
	"0 Golden Obi": {"base": "Golden Obi", "type": "unique extremely high"},
	"0 Golden Wreath": {"base": "Golden Wreath", "type": "unique extremely high"},
	"0 Grand Mana Flask": {"base": "Grand Mana Flask", "type": "unique extremely high"},
	"0 Greatwolf Talisman": {"base": "Greatwolf Talisman", "type": "unique extremely high"},
	"0 Harlequin Mask": {"base": "Harlequin Mask", "type": "unique extremely high"},
	"0 Hydrascale Gauntlets": {"base": "Hydrascale Gauntlets", "type": "unique extremely high"},
	"0 Jet Amulet": {"base": "Jet Amulet", "type": "unique extremely high"},
	"0 Legion Gloves": {"base": "Legion Gloves", "type": "unique extremely high"},
	"0 Maze Map": {"base": "Maze Map", "type": "unique extremely high"},
	"0 Prismatic Jewel": {"base": "Prismatic Jewel", "type": "unique extremely high"},
	"0 Prophecy Wand": {"base": "Prophecy Wand", "type": "unique extremely high"},
	"0 Rawhide Boots": {"base": "Rawhide Boots", "type": "unique extremely high"},
	"0 Riveted Gloves": {"base": "Riveted Gloves", "type": "unique extremely high"},
	"0 Rotfeather Talisman": {"base": "Rotfeather Talisman", "type": "unique extremely high"},
	"0 Royal Axe": {"base": "Royal Axe", "type": "unique extremely high"},
	"0 Satin Gloves": {"base": "Satin Gloves", "type": "unique extremely high"},
	"1 Arcanist Gloves": {"base": "Arcanist Gloves", "type": "unique very high"},
	"1 Arcanist Slippers": {"base": "Arcanist Slippers", "type": "unique very high"},
	"1 Assassin's Boots": {"base": "Assassin's Boots", "type": "unique very high"},
	"1 Blood Raiment": {"base": "Blood Raiment", "type": "unique very high"},
	"1 Blunt Arrow Quiver Piece": {"base": "Blunt Arrow Quiver Piece", "type": "unique very high"},
	"1 Callous Mask Piece": {"base": "Callous Mask Piece", "type": "unique very high"},
	"1 Carnal Sceptre": {"base": "Carnal Sceptre", "type": "unique very high"},
	"1 Clutching Talisman": {"base": "Clutching Talisman", "type": "unique very high"},
	"1 Courtyard Map": {"base": "Courtyard Map", "type": "unique very high"},
	"1 Cured Quiver": {"base": "Cured Quiver", "type": "unique very high"},
	"1 Deicide Mask": {"base": "Deicide Mask", "type": "unique very high"},
	"1 Gemstone Sword": {"base": "Gemstone Sword", "type": "unique very high"},
	"1 Gladiator Plate": {"base": "Gladiator Plate", "type": "unique very high"},
	"1 Glorious Plate": {"base": "Glorious Plate", "type": "unique very high"},
	"1 Harbinger Map": {"base": "Harbinger Map", "type": "unique very high"},
	"1 Heavy Quiver": {"base": "Heavy Quiver", "type": "unique very high"},
	"1 Hydrascale Boots": {"base": "Hydrascale Boots", "type": "unique very high"},
	"1 Imperial Maul": {"base": "Imperial Maul", "type": "unique very high"},
	"1 Jewelled Foil": {"base": "Jewelled Foil", "type": "unique very high"},
	"1 Magistrate Crown": {"base": "Magistrate Crown", "type": "unique very high"},
	"1 Moon Temple Map": {"base": "Moon Temple Map", "type": "unique very high"},
	"1 Museum Map": {"base": "Museum Map", "type": "unique very high"},
	"1 Nightmare Mace": {"base": "Nightmare Mace", "type": "unique very high"},
	"1 Nubuck Gloves": {"base": "Nubuck Gloves", "type": "unique very high"},
	"1 Rawhide Tower Shield": {"base": "Rawhide Tower Shield", "type": "unique very high"},
	"1 Ritual Sceptre": {"base": "Ritual Sceptre", "type": "unique very high"},
	"1 Ruby Amulet": {"base": "Ruby Amulet", "type": "unique very high"},
	"1 Sacrificial Garb": {"base": "Sacrificial Garb", "type": "unique very high"},
	"1 Sanctified Life Flask": {"base": "Sanctified Life Flask", "type": "unique very high"},
	"1 Sanctified Mana Flask": {"base": "Sanctified Mana Flask", "type": "unique very high"},
	"1 Sapphire Flask": {"base": "Sapphire Flask", "type": "unique very high"},
	"1 Sharkskin Tunic": {"base": "Sharkskin Tunic", "type": "unique very high"},
	"1 Shore Map": {"base": "Shore Map", "type": "unique very high"},
	"1 Siege Axe": {"base": "Siege Axe", "type": "unique very high"},
	"1 Steel Ring": {"base": "Steel Ring", "type": "unique very high"},
	"1 Steelhead": {"base": "Steelhead", "type": "unique very high"},
	"1 Temple Map": {"base": "Temple Map", "type": "unique very high"},
	"1 Topaz Flask": {"base": "Topaz Flask", "type": "unique very high"},
	"1 Vaal Mask": {"base": "Vaal Mask", "type": "unique very high"},
	"1 Variscite Blade": {"base": "Variscite Blade", "type": "unique very high"},
	"1 Void Axe": {"base": "Void Axe", "type": "unique very high"},
	"1 Wereclaw Talisman": {"base": "Wereclaw Talisman", "type": "unique very high"},
	"1 Wyrmscale Doublet": {"base": "Wyrmscale Doublet", "type": "unique very high"},
	"1 Zealot Gloves": {"base": "Zealot Gloves", "type": "unique very high"},
	"2 Abyssal Axe": {"base": "Abyssal Axe", "type": "unique high"},
	"2 Amethyst Flask": {"base": "Amethyst Flask", "type": "unique high"},
	"2 Ancient Gauntlets": {"base": "Ancient Gauntlets", "type": "unique high"},
	"2 Assassin's Garb": {"base": "Assassin's Garb", "type": "unique high"},
	"2 Astral Plate": {"base": "Astral Plate", "type": "unique high"},
	"2 Atoll Map": {"base": "Atoll Map", "type": "unique high"},
	"2 Bismuth Flask": {"base": "Bismuth Flask", "type": "unique high"},
	"2 Black Maw Talisman": {"base": "Black Maw Talisman", "type": "unique high"},
	"2 Blinder": {"base": "Blinder", "type": "unique high"},
	"2 Blue Pearl Amulet": {"base": "Blue Pearl Amulet", "type": "unique high"},
	"2 Bone Armour": {"base": "Bone Armour", "type": "unique high"},
	"2 Bone Crypt Map": {"base": "Bone Crypt Map", "type": "unique high"},
	"2 Brass Spirit Shield": {"base": "Brass Spirit Shield", "type": "unique high"},
	"2 Broadhead Arrow Quiver": {"base": "Broadhead Arrow Quiver", "type": "unique high"},
	"2 Cardinal Round Shield": {"base": "Cardinal Round Shield", "type": "unique high"},
	"2 Cedar Tower Shield": {"base": "Cedar Tower Shield", "type": "unique high"},
	"2 Cemetery Map": {"base": "Cemetery Map", "type": "unique high"},
	"2 Clasped Mitts": {"base": "Clasped Mitts", "type": "unique high"},
	"2 Close Helmet": {"base": "Close Helmet", "type": "unique high"},
	"2 Colossal Tower Shield": {"base": "Colossal Tower Shield", "type": "unique high"},
	"2 Conjurer Boots": {"base": "Conjurer Boots", "type": "unique high"},
	"2 Conjurer Gloves": {"base": "Conjurer Gloves", "type": "unique high"},
	"2 Corrugated Buckler": {"base": "Corrugated Buckler", "type": "unique high"},
	"2 Corsair Sword": {"base": "Corsair Sword", "type": "unique high"},
	"2 Crusader Chainmail": {"base": "Crusader Chainmail", "type": "unique high"},
	"2 Crusader Helmet": {"base": "Crusader Helmet", "type": "unique high"},
	"2 Crystal Belt": {"base": "Crystal Belt", "type": "unique high"},
	"2 Cursed Crypt Map": {"base": "Cursed Crypt Map", "type": "unique high"},
	"2 Demon Dagger": {"base": "Demon Dagger", "type": "unique high"},
	"2 Destiny Leather": {"base": "Destiny Leather", "type": "unique high"},
	"2 Destroyer Regalia": {"base": "Destroyer Regalia", "type": "unique high"},
	"2 Diamond Flask": {"base": "Diamond Flask", "type": "unique high"},
	"2 Dragonscale Boots": {"base": "Dragonscale Boots", "type": "unique high"},
	"2 Dunes Map": {"base": "Dunes Map", "type": "unique high"},
	"2 Elder Sword": {"base": "Elder Sword", "type": "unique high"},
	"2 Elegant Foil": {"base": "Elegant Foil", "type": "unique high"},
	"2 Engraved Wand": {"base": "Engraved Wand", "type": "unique high"},
	"2 Eternal Sword": {"base": "Eternal Sword", "type": "unique high"},
	"2 Eye Gouger": {"base": "Eye Gouger", "type": "unique high"},
	"2 Ezomyte Blade": {"base": "Ezomyte Blade", "type": "unique high"},
	"2 Ezomyte Burgonet": {"base": "Ezomyte Burgonet", "type": "unique high"},
	"2 Festival Mask": {"base": "Festival Mask", "type": "unique high"},
	"2 Full Scale Armour": {"base": "Full Scale Armour", "type": "unique high"},
	"2 Full Wyrmscale": {"base": "Full Wyrmscale", "type": "unique high"},
	"2 Gladius": {"base": "Gladius", "type": "unique high"},
	"2 Goathide Gloves": {"base": "Goathide Gloves", "type": "unique high"},
	"2 Goliath Gauntlets": {"base": "Goliath Gauntlets", "type": "unique high"},
	"2 Hallowed Hybrid Flask": {"base": "Hallowed Hybrid Flask", "type": "unique high"},
	"2 Hellion's Paw": {"base": "Hellion's Paw", "type": "unique high"},
	"2 Highborn Staff": {"base": "Highborn Staff", "type": "unique high"},
	"2 Iron Gauntlets": {"base": "Iron Gauntlets", "type": "unique high"},
	"2 Iron Ring": {"base": "Iron Ring", "type": "unique high"},
	"2 Iron Sceptre": {"base": "Iron Sceptre", "type": "unique high"},
	"2 Jingling Spirit Shield": {"base": "Jingling Spirit Shield", "type": "unique high"},
	"2 Karui Sceptre": {"base": "Karui Sceptre", "type": "unique high"},
	"2 Labrys": {"base": "Labrys", "type": "unique high"},
	"2 Leather Cap": {"base": "Leather Cap", "type": "unique high"},
	"2 Leatherscale Boots": {"base": "Leatherscale Boots", "type": "unique high"},
	"2 Lion Pelt": {"base": "Lion Pelt", "type": "unique high"},
	"2 Lion Sword": {"base": "Lion Sword", "type": "unique high"},
	"2 Marble Amulet": {"base": "Marble Amulet", "type": "unique high"},
	"2 Meatgrinder": {"base": "Meatgrinder", "type": "unique high"},
	"2 Mirrored Spiked Shield": {"base": "Mirrored Spiked Shield", "type": "unique high"},
	"2 Murder Mitts": {"base": "Murder Mitts", "type": "unique high"},
	"2 Necromancer Silks": {"base": "Necromancer Silks", "type": "unique high"},
	"2 Necropolis Map": {"base": "Necropolis Map", "type": "unique high"},
	"2 Opal Sceptre": {"base": "Opal Sceptre", "type": "unique high"},
	"2 Opal Wand": {"base": "Opal Wand", "type": "unique high"},
	"2 Overgrown Shrine Map": {"base": "Overgrown Shrine Map", "type": "unique high"},
	"2 Platinum Sceptre": {"base": "Platinum Sceptre", "type": "unique high"},
	"2 Polished Spiked Shield": {"base": "Polished Spiked Shield", "type": "unique high"},
	"2 Promenade Map": {"base": "Promenade Map", "type": "unique high"},
	"2 Reinforced Greaves": {"base": "Reinforced Greaves", "type": "unique high"},
	"2 Ruby Ring": {"base": "Ruby Ring", "type": "unique high"},
	"2 Sabre": {"base": "Sabre", "type": "unique high"},
	"2 Sapphire Ring": {"base": "Sapphire Ring", "type": "unique high"},
	"2 Savant's Robe": {"base": "Savant's Robe", "type": "unique high"},
	"2 Serpentscale Gauntlets": {"base": "Serpentscale Gauntlets", "type": "unique high"},
	"2 Siege Helmet": {"base": "Siege Helmet", "type": "unique high"},
	"2 Silver Flask": {"base": "Silver Flask", "type": "unique high"},
	"2 Sinner Tricorne": {"base": "Sinner Tricorne", "type": "unique high"},
	"2 Soldier Boots": {"base": "Soldier Boots", "type": "unique high"},
	"2 Sorcerer Gloves": {"base": "Sorcerer Gloves", "type": "unique high"},
	"2 Spine Bow": {"base": "Spine Bow", "type": "unique high"},
	"2 Strand Map": {"base": "Strand Map", "type": "unique high"},
	"2 Stygian Vise": {"base": "Stygian Vise", "type": "unique high"},
	"2 Terror Claw": {"base": "Terror Claw", "type": "unique high"},
	"2 Terror Maul": {"base": "Terror Maul", "type": "unique high"},
	"2 Thorium Spirit Shield": {"base": "Thorium Spirit Shield", "type": "unique high"},
	"2 Throat Stabber": {"base": "Throat Stabber", "type": "unique high"},
	"2 Tiger Sword": {"base": "Tiger Sword", "type": "unique high"},
	"2 Titanium Spirit Shield": {"base": "Titanium Spirit Shield", "type": "unique high"},
	"2 Torture Chamber Map": {"base": "Torture Chamber Map", "type": "unique high"},
	"2 Trapper Boots": {"base": "Trapper Boots", "type": "unique high"},
	"2 Underground River Map": {"base": "Underground River Map", "type": "unique high"},
	"2 Ursine Pelt": {"base": "Ursine Pelt", "type": "unique high"},
	"2 Vaal Pyramid Map": {"base": "Vaal Pyramid Map", "type": "unique high"},
	"2 Vanguard Belt": {"base": "Vanguard Belt", "type": "unique high"},
	"2 Varnished Coat": {"base": "Varnished Coat", "type": "unique high"},
	"2 War Sword": {"base": "War Sword", "type": "unique high"},
	"2 Wool Shoes": {"base": "Wool Shoes", "type": "unique high"},
	"2 Zealot Helmet": {"base": "Zealot Helmet", "type": "unique high"},
	"6 Agate Amulet": {"base": "Agate Amulet", "type": "unique special"},
	"6 Amber Amulet": {"base": "Amber Amulet", "type": "unique special"},
	"6 Amethyst Ring": {"base": "Amethyst Ring", "type": "unique special"},
	"6 Ancient Greaves": {"base": "Ancient Greaves", "type": "unique special"},
	"6 Ancient Spirit Shield": {"base": "Ancient Spirit Shield", "type": "unique special"},
	"6 Archon Kite Shield": {"base": "Archon Kite Shield", "type": "unique special"},
	"6 Archon Kite Shield Piece": {"base": "Archon Kite Shield Piece", "type": "unique special"},
	"6 Assassin Bow": {"base": "Assassin Bow", "type": "unique special"},
	"6 Blunt Arrow Quiver": {"base": "Blunt Arrow Quiver", "type": "unique special"},
	"6 Bone Bow": {"base": "Bone Bow", "type": "unique special"},
	"6 Branded Kite Shield": {"base": "Branded Kite Shield", "type": "unique special"},
	"6 Carnal Armour": {"base": "Carnal Armour", "type": "unique special"},
	"6 Carnal Mitts": {"base": "Carnal Mitts", "type": "unique special"},
	"6 Carved Wand": {"base": "Carved Wand", "type": "unique special"},
	"6 Chain Belt": {"base": "Chain Belt", "type": "unique special"},
	"6 Champion Kite Shield": {"base": "Champion Kite Shield", "type": "unique special"},
	"6 Citadel Bow": {"base": "Citadel Bow", "type": "unique special"},
	"6 Citrine Amulet": {"base": "Citrine Amulet", "type": "unique special"},
	"6 Cloth Belt": {"base": "Cloth Belt", "type": "unique special"},
	"6 Cloth Belt Piece": {"base": "Cloth Belt Piece", "type": "unique special"},
	"6 Cobalt Jewel": {"base": "Cobalt Jewel", "type": "unique special"},
	"6 Coral Amulet": {"base": "Coral Amulet", "type": "unique special"},
	"6 Coral Ring": {"base": "Coral Ring", "type": "unique special"},
	"6 Coronal Leather": {"base": "Coronal Leather", "type": "unique special"},
	"6 Crimson Jewel": {"base": "Crimson Jewel", "type": "unique special"},
	"6 Crude Bow": {"base": "Crude Bow", "type": "unique special"},
	"6 Crusader Gloves": {"base": "Crusader Gloves", "type": "unique special"},
	"6 Cutlass": {"base": "Cutlass", "type": "unique special"},
	"6 Deerskin Gloves": {"base": "Deerskin Gloves", "type": "unique special"},
	"6 Despot Axe": {"base": "Despot Axe", "type": "unique special"},
	"6 Diamond Ring": {"base": "Diamond Ring", "type": "unique special"},
	"6 Dusk Blade": {"base": "Dusk Blade", "type": "unique special"},
	"6 Ebony Tower Shield": {"base": "Ebony Tower Shield", "type": "unique special"},
	"6 Elegant Ringmail": {"base": "Elegant Ringmail", "type": "unique special"},
	"6 Elegant Sword": {"base": "Elegant Sword", "type": "unique special"},
	"6 Etched Greatsword": {"base": "Etched Greatsword", "type": "unique special"},
	"6 Exquisite Leather": {"base": "Exquisite Leather", "type": "unique special"},
	"6 Ezomyte Staff": {"base": "Ezomyte Staff", "type": "unique special"},
	"6 Gavel": {"base": "Gavel", "type": "unique special"},
	"6 Goathide Boots": {"base": "Goathide Boots", "type": "unique special"},
	"6 Gold Amulet": {"base": "Gold Amulet", "type": "unique special"},
	"6 Gold Ring": {"base": "Gold Ring", "type": "unique special"},
	"6 Golden Plate": {"base": "Golden Plate", "type": "unique special"},
	"6 Goliath Greaves": {"base": "Goliath Greaves", "type": "unique special"},
	"6 Granite Flask": {"base": "Granite Flask", "type": "unique special"},
	"6 Great Crown": {"base": "Great Crown", "type": "unique special"},
	"6 Great Mallet": {"base": "Great Mallet", "type": "unique special"},
	"6 Heavy Belt": {"base": "Heavy Belt", "type": "unique special"},
	"6 Hubris Circlet": {"base": "Hubris Circlet", "type": "unique special"},
	"6 Imbued Wand": {"base": "Imbued Wand", "type": "unique special"},
	"6 Imperial Bow": {"base": "Imperial Bow", "type": "unique special"},
	"6 Imperial Claw": {"base": "Imperial Claw", "type": "unique special"},
	"6 Imperial Staff": {"base": "Imperial Staff", "type": "unique special"},
	"6 Infernal Sword": {"base": "Infernal Sword", "type": "unique special"},
	"6 Ironscale Gauntlets": {"base": "Ironscale Gauntlets", "type": "unique special"},
	"6 Jade Amulet": {"base": "Jade Amulet", "type": "unique special"},
	"6 Jasper Chopper": {"base": "Jasper Chopper", "type": "unique special"},
	"6 Judgement Staff": {"base": "Judgement Staff", "type": "unique special"},
	"6 Lacquered Garb": {"base": "Lacquered Garb", "type": "unique special"},
	"6 Lapis Amulet": {"base": "Lapis Amulet", "type": "unique special"},
	"6 Large Hybrid Flask": {"base": "Large Hybrid Flask", "type": "unique special"},
	"6 Leather Belt": {"base": "Leather Belt", "type": "unique special"},
	"6 Legion Sword": {"base": "Legion Sword", "type": "unique special"},
	"6 Long Staff": {"base": "Long Staff", "type": "unique special"},
	"6 Maelström Staff": {"base": "Maelström Staff", "type": "unique special"},
	"6 Midnight Blade": {"base": "Midnight Blade", "type": "unique special"},
	"6 Mind Cage": {"base": "Mind Cage", "type": "unique special"},
	"6 Moonstone Ring": {"base": "Moonstone Ring", "type": "unique special"},
	"6 Mosaic Kite Shield": {"base": "Mosaic Kite Shield", "type": "unique special"},
	"6 Murder Boots": {"base": "Murder Boots", "type": "unique special"},
	"6 Necromancer Circlet": {"base": "Necromancer Circlet", "type": "unique special"},
	"6 Nightmare Bascinet": {"base": "Nightmare Bascinet", "type": "unique special"},
	"6 Nubuck Boots": {"base": "Nubuck Boots", "type": "unique special"},
	"6 Occultist's Vestment": {"base": "Occultist's Vestment", "type": "unique special"},
	"6 Onyx Amulet": {"base": "Onyx Amulet", "type": "unique special"},
	"6 Opal Ring": {"base": "Opal Ring", "type": "unique special"},
	"6 Painted Tower Shield": {"base": "Painted Tower Shield", "type": "unique special"},
	"6 Paua Amulet": {"base": "Paua Amulet", "type": "unique special"},
	"6 Paua Ring": {"base": "Paua Ring", "type": "unique special"},
	"6 Penetrating Arrow Quiver": {"base": "Penetrating Arrow Quiver", "type": "unique special"},
	"6 Pine Buckler": {"base": "Pine Buckler", "type": "unique special"},
	"6 Pinnacle Tower Shield": {"base": "Pinnacle Tower Shield", "type": "unique special"},
	"6 Plank Kite Shield": {"base": "Plank Kite Shield", "type": "unique special"},
	"6 Prismatic Ring": {"base": "Prismatic Ring", "type": "unique special"},
	"6 Quartz Flask": {"base": "Quartz Flask", "type": "unique special"},
	"6 Raven Mask": {"base": "Raven Mask", "type": "unique special"},
	"6 Regicide Mask": {"base": "Regicide Mask", "type": "unique special"},
	"6 Royal Burgonet": {"base": "Royal Burgonet", "type": "unique special"},
	"6 Ruby Flask": {"base": "Ruby Flask", "type": "unique special"},
	"6 Rustic Sash": {"base": "Rustic Sash", "type": "unique special"},
	"6 Sadist Garb": {"base": "Sadist Garb", "type": "unique special"},
	"6 Sage Wand": {"base": "Sage Wand", "type": "unique special"},
	"6 Saintly Chainmail": {"base": "Saintly Chainmail", "type": "unique special"},
	"6 Shackled Boots": {"base": "Shackled Boots", "type": "unique special"},
	"6 Sharkskin Boots": {"base": "Sharkskin Boots", "type": "unique special"},
	"6 Silken Hood": {"base": "Silken Hood", "type": "unique special"},
	"6 Slink Boots": {"base": "Slink Boots", "type": "unique special"},
	"6 Soldier Gloves": {"base": "Soldier Gloves", "type": "unique special"},
	"6 Sorcerer Boots": {"base": "Sorcerer Boots", "type": "unique special"},
	"6 Spidersilk Robe": {"base": "Spidersilk Robe", "type": "unique special"},
	"6 Spike-Point Arrow Quiver": {"base": "Spike-Point Arrow Quiver", "type": "unique special"},
	"6 Stealth Boots": {"base": "Stealth Boots", "type": "unique special"},
	"6 Steelscale Gauntlets": {"base": "Steelscale Gauntlets", "type": "unique special"},
	"6 Stibnite Flask": {"base": "Stibnite Flask", "type": "unique special"},
	"6 Strapped Mitts": {"base": "Strapped Mitts", "type": "unique special"},
	"6 Sundering Axe": {"base": "Sundering Axe", "type": "unique special"},
	"6 Tarnished Spirit Shield": {"base": "Tarnished Spirit Shield", "type": "unique special"},
	"6 Thresher Claw": {"base": "Thresher Claw", "type": "unique special"},
	"6 Titan Gauntlets": {"base": "Titan Gauntlets", "type": "unique special"},
	"6 Titan Greaves": {"base": "Titan Greaves", "type": "unique special"},
	"6 Topaz Ring": {"base": "Topaz Ring", "type": "unique special"},
	"6 Tornado Wand": {"base": "Tornado Wand", "type": "unique special"},
	"6 Triumphant Lamellar": {"base": "Triumphant Lamellar", "type": "unique special"},
	"6 Turquoise Amulet": {"base": "Turquoise Amulet", "type": "unique special"},
	"6 Two-Point Arrow Quiver": {"base": "Two-Point Arrow Quiver", "type": "unique special"},
	"6 Two-Stone Ring": {"base": "Two-Stone Ring", "type": "unique special"},
	"6 Unset Ring": {"base": "Unset Ring", "type": "unique special"},
	"6 Vaal Axe": {"base": "Vaal Axe", "type": "unique special"},
	"6 Vaal Blade": {"base": "Vaal Blade", "type": "unique special"},
	"6 Vaal Gauntlets": {"base": "Vaal Gauntlets", "type": "unique special"},
	"6 Vaal Sceptre": {"base": "Vaal Sceptre", "type": "unique special"},
	"6 Vaal Spirit Shield": {"base": "Vaal Spirit Shield", "type": "unique special"},
	"6 Velvet Slippers": {"base": "Velvet Slippers", "type": "unique special"},
	"6 Viridian Jewel": {"base": "Viridian Jewel", "type": "unique special"},
	"6 Widowsilk Robe": {"base": "Widowsilk Robe", "type": "unique special"},
	"6 Wool Gloves": {"base": "Wool Gloves", "type": "unique special"},
	"6 Zodiac Leather": {"base": "Zodiac Leather", "type": "unique special"},
	"9 Other uniques": {"type": "unique normal"}
}
