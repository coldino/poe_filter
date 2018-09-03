#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/03/2018(m/d/y) 22:13:03 UTC from "Hardcore" data

desc = "Currency Autogen"

# Base type : settings pair
items = {
	"0 Aberrant Fossil": {"base": "Aberrant Fossil", "class": "Currency", "type": "currency normal"},
	"0 Aetheric Fossil": {"base": "Aetheric Fossil", "class": "Currency", "type": "currency high"},
	"0 Alchemy Shard": {"base": "Alchemy Shard", "class": "Currency", "type": "currency very low"},
	"0 Alteration Shard": {"base": "Alteration Shard", "class": "Currency", "type": "currency very low"},
	"0 Ancient Orb": {"base": "Ancient Orb", "class": "Currency", "type": "currency very high"},
	"0 Ancient Shard": {"base": "Ancient Shard", "class": "Currency", "type": "currency high"},
	"0 Annulment Shard": {"base": "Annulment Shard", "class": "Currency", "type": "currency normal"},
	"0 Apprentice Cartographer's Sextant": {"base": "Apprentice Cartographer's Sextant", "class": "Currency", "type": "currency high"},
	"0 Armourer's Scrap": {"base": "Armourer's Scrap", "class": "Currency", "type": "currency very low"},
	"0 Binding Shard": {"base": "Binding Shard", "class": "Currency", "type": "currency low"},
	"0 Blacksmith's Whetstone": {"base": "Blacksmith's Whetstone", "class": "Currency", "type": "currency very low"},
	"0 Blessed Orb": {"base": "Blessed Orb", "class": "Currency", "type": "currency high"},
	"0 Blessing of Chayula": {"base": "Blessing of Chayula", "class": "Currency", "type": "currency extremely high"},
	"0 Blessing of Esh": {"base": "Blessing of Esh", "class": "Currency", "type": "currency very high"},
	"0 Blessing of Tul": {"base": "Blessing of Tul", "class": "Currency", "type": "currency very high"},
	"0 Blessing of Uul-Netol": {"base": "Blessing of Uul-Netol", "class": "Currency", "type": "currency extremely high"},
	"0 Blessing of Xoph": {"base": "Blessing of Xoph", "class": "Currency", "type": "currency high"},
	"0 Bloodstained Fossil": {"base": "Bloodstained Fossil", "class": "Currency", "type": "currency very high"},
	"0 Bound Fossil": {"base": "Bound Fossil", "class": "Currency", "type": "currency high"},
	"0 Cartographer's Chisel": {"base": "Cartographer's Chisel", "class": "Currency", "type": "currency normal"},
	"0 Chaos Orb": {"base": "Chaos Orb", "class": "Currency", "type": "currency high"},
	"0 Chaos Shard": {"base": "Chaos Shard", "class": "Currency", "type": "currency very low"},
	"0 Chromatic Orb": {"base": "Chromatic Orb", "class": "Currency", "type": "currency show"},
	"0 Corroded Fossil": {"base": "Corroded Fossil", "class": "Currency", "type": "currency high"},
	"0 Dense Fossil": {"base": "Dense Fossil", "class": "Currency", "type": "currency normal"},
	"0 Divine Orb": {"base": "Divine Orb", "class": "Currency", "type": "currency very high"},
	"0 Enchanted Fossil": {"base": "Enchanted Fossil", "class": "Currency", "type": "currency high"},
	"0 Encrusted Fossil": {"base": "Encrusted Fossil", "class": "Currency", "type": "currency high"},
	"0 Engineer's Orb": {"base": "Engineer's Orb", "class": "Currency", "type": "currency normal"},
	"0 Engineer's Shard": {"base": "Engineer's Shard", "class": "Currency", "type": "currency low"},
	"0 Eternal Orb": {"base": "Eternal Orb", "class": "Currency", "type": "currency extremely high"},
	"0 Exalted Orb": {"base": "Exalted Orb", "class": "Currency", "type": "currency very high"},
	"0 Exalted Shard": {"base": "Exalted Shard", "class": "Currency", "type": "currency high"},
	"0 Faceted Fossil": {"base": "Faceted Fossil", "class": "Currency", "type": "currency very high"},
	"0 Fractured Fossil ": {"base": "Fractured Fossil ", "class": "Currency", "type": "currency extremely high"},
	"0 Frigid Fossil": {"base": "Frigid Fossil", "class": "Currency", "type": "currency normal"},
	"0 Gemcutter's Prism": {"base": "Gemcutter's Prism", "class": "Currency", "type": "currency high"},
	"0 Gilded Fossil": {"base": "Gilded Fossil", "class": "Currency", "type": "currency very high"},
	"0 Glassblower's Bauble": {"base": "Glassblower's Bauble", "class": "Currency", "type": "currency normal"},
	"0 Glyphic Fossil": {"base": "Glyphic Fossil", "class": "Currency", "type": "currency very high"},
	"0 Harbinger's Orb": {"base": "Harbinger's Orb", "class": "Currency", "type": "currency high"},
	"0 Harbinger's Shard": {"base": "Harbinger's Shard", "class": "Currency", "type": "currency normal"},
	"0 Hollow Fossil": {"base": "Hollow Fossil", "class": "Currency", "type": "currency very high"},
	"0 Horizon Shard": {"base": "Horizon Shard", "class": "Currency", "type": "currency high"},
	"0 Jagged Fossil": {"base": "Jagged Fossil", "class": "Currency", "type": "currency high"},
	"0 Jeweller's Orb": {"base": "Jeweller's Orb", "class": "Currency", "type": "currency show"},
	"0 Journeyman Cartographer's Sextant": {"base": "Journeyman Cartographer's Sextant", "class": "Currency", "type": "currency high"},
	"0 Lucent Fossil": {"base": "Lucent Fossil", "class": "Currency", "type": "currency high"},
	"0 Master Cartographer's Sextant": {"base": "Master Cartographer's Sextant", "class": "Currency", "type": "currency high"},
	"0 Metallic Fossil": {"base": "Metallic Fossil", "class": "Currency", "type": "currency normal"},
	"0 Mirror Shard": {"base": "Mirror Shard", "class": "Currency", "type": "currency extremely high"},
	"0 Mirror of Kalandra": {"base": "Mirror of Kalandra", "class": "Currency", "type": "currency extremely high"},
	"0 Orb of Alchemy": {"base": "Orb of Alchemy", "class": "Currency", "type": "currency normal"},
	"0 Orb of Alteration": {"base": "Orb of Alteration", "class": "Currency", "type": "currency low"},
	"0 Orb of Annulment": {"base": "Orb of Annulment", "class": "Currency", "type": "currency very high"},
	"0 Orb of Augmentation": {"base": "Orb of Augmentation", "class": "Currency", "type": "currency very low"},
	"0 Orb of Binding": {"base": "Orb of Binding", "class": "Currency", "type": "currency normal"},
	"0 Orb of Chance": {"base": "Orb of Chance", "class": "Currency", "type": "currency show"},
	"0 Orb of Fusing": {"base": "Orb of Fusing", "class": "Currency", "type": "currency normal"},
	"0 Orb of Horizons": {"base": "Orb of Horizons", "class": "Currency", "type": "currency very high"},
	"0 Orb of Regret": {"base": "Orb of Regret", "class": "Currency", "type": "currency normal"},
	"0 Orb of Scouring": {"base": "Orb of Scouring", "class": "Currency", "type": "currency normal"},
	"0 Orb of Transmutation": {"base": "Orb of Transmutation", "class": "Currency", "type": "currency very low"},
	"0 Perandus Coin": {"base": "Perandus Coin", "class": "Currency", "type": "currency show"},
	"0 Perfect Fossil": {"base": "Perfect Fossil", "class": "Currency", "type": "currency high"},
	"0 Portal Scroll": {"base": "Portal Scroll", "class": "Currency", "type": "currency very low"},
	"0 Potent Alchemical Resonator": {"base": "Potent Alchemical Resonator", "class": "Currency", "type": "currency normal"},
	"0 Potent Chaotic Resonator": {"base": "Potent Chaotic Resonator", "class": "Currency", "type": "currency normal"},
	"0 Powerful Alchemical Resonator": {"base": "Powerful Alchemical Resonator", "class": "Currency", "type": "currency high"},
	"0 Powerful Chaotic Resonator": {"base": "Powerful Chaotic Resonator", "class": "Currency", "type": "currency high"},
	"0 Prime Alchemical Resonator": {"base": "Prime Alchemical Resonator", "class": "Currency", "type": "currency very high"},
	"0 Prime Chaotic Resonator": {"base": "Prime Chaotic Resonator", "class": "Currency", "type": "currency very high"},
	"0 Primitive Alchemical Resonator": {"base": "Primitive Alchemical Resonator", "class": "Currency", "type": "currency normal"},
	"0 Primitive Chaotic Resonator": {"base": "Primitive Chaotic Resonator", "class": "Currency", "type": "currency normal"},
	"0 Prismatic Fossil": {"base": "Prismatic Fossil", "class": "Currency", "type": "currency high"},
	"0 Pristine Fossil": {"base": "Pristine Fossil", "class": "Currency", "type": "currency high"},
	"0 Regal Orb": {"base": "Regal Orb", "class": "Currency", "type": "currency high"},
	"0 Regal Shard": {"base": "Regal Shard", "class": "Currency", "type": "currency low"},
	"0 Sanctified Fossil": {"base": "Sanctified Fossil", "class": "Currency", "type": "currency very high"},
	"0 Scorched Fossil": {"base": "Scorched Fossil", "class": "Currency", "type": "currency high"},
	"0 Scroll Fragment": {"base": "Scroll Fragment", "class": "Currency", "type": "currency very low"},
	"0 Scroll of Wisdom": {"base": "Scroll of Wisdom", "class": "Currency", "type": "currency very low"},
	"0 Serrated Fossil": {"base": "Serrated Fossil", "class": "Currency", "type": "currency high"},
	"0 Shuddering Fossil": {"base": "Shuddering Fossil", "class": "Currency", "type": "currency very high"},
	"0 Silver Coin": {"base": "Silver Coin", "class": "Currency", "type": "currency normal"},
	"0 Splinter of Chayula": {"base": "Splinter of Chayula", "class": "Currency", "type": "currency high"},
	"0 Splinter of Esh": {"base": "Splinter of Esh", "class": "Currency", "type": "currency high"},
	"0 Splinter of Tul": {"base": "Splinter of Tul", "class": "Currency", "type": "currency high"},
	"0 Splinter of Uul-Netol": {"base": "Splinter of Uul-Netol", "class": "Currency", "type": "currency high"},
	"0 Splinter of Xoph": {"base": "Splinter of Xoph", "class": "Currency", "type": "currency high"},
	"0 Tangled Fossil": {"base": "Tangled Fossil", "class": "Currency", "type": "currency very high"},
	"0 Transmutation Shard": {"base": "Transmutation Shard", "class": "Currency", "type": "currency very low"},
	"0 Vaal Orb": {"base": "Vaal Orb", "class": "Currency", "type": "currency normal"},
}
