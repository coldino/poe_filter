#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 12/10/2018(m/d/y) 22:08:13 UTC from "tmphardcore" data

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 Beauty Through Death": {"base": "Beauty Through Death", "class": "Divination Card", "type": "divination extremely high"},
	"001 The Master Artisan": {"base": "The Master Artisan", "class": "Divination Card", "type": "divination normal"},
	"002 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"003 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination normal"},
	"004 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination normal"},
	"005 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"1 A Dab of Ink": {"base": "A Dab of Ink", "class": "Divination Card", "type": "divination very high"},
	"1 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination low"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination low"},
	"1 Blessing of God": {"base": "Blessing of God", "class": "Divination Card", "type": "hide"},
	"1 Boon of the First Ones": {"base": "Boon of the First Ones", "class": "Divination Card", "type": "divination very high"},
	"1 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination high"},
	"1 Call to the First Ones": {"base": "Call to the First Ones", "class": "Divination Card", "type": "divination low"},
	"1 Chaotic Disposition": {"base": "Chaotic Disposition", "class": "Divination Card", "type": "divination very high"},
	"1 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "hide"},
	"1 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination high"},
	"1 Forbidden Power": {"base": "Forbidden Power", "class": "Divination Card", "type": "divination high"},
	"1 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination extremely high"},
	"1 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"1 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination extremely high"},
	"1 Immortal Resolve": {"base": "Immortal Resolve", "class": "Divination Card", "type": "divination extremely high"},
	"1 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"1 Left to Fate": {"base": "Left to Fate", "class": "Divination Card", "type": "divination high"},
	"1 Lingering Remnants": {"base": "Lingering Remnants", "class": "Divination Card", "type": "divination high"},
	"1 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination high"},
	"1 Mawr Blaidd": {"base": "Mawr Blaidd", "class": "Divination Card", "type": "divination extremely high"},
	"1 Merciless Armament": {"base": "Merciless Armament", "class": "Divination Card", "type": "hide"},
	"1 Might is Right": {"base": "Might is Right", "class": "Divination Card", "type": "divination high"},
	"1 Perfection": {"base": "Perfection", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "hide"},
	"1 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "hide"},
	"1 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"1 Struck by Lightning": {"base": "Struck by Lightning", "class": "Divination Card", "type": "hide"},
	"1 The Admirer": {"base": "The Admirer", "class": "Divination Card", "type": "divination high"},
	"1 The Artist": {"base": "The Artist", "class": "Divination Card", "type": "divination very high"},
	"1 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"1 The Beast": {"base": "The Beast", "class": "Divination Card", "type": "divination high"},
	"1 The Blazing Fire": {"base": "The Blazing Fire", "class": "Divination Card", "type": "divination low"},
	"1 The Breach": {"base": "The Breach", "class": "Divination Card", "type": "divination high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"1 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"1 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Stone": {"base": "The Celestial Stone", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"1 The Coming Storm": {"base": "The Coming Storm", "class": "Divination Card", "type": "divination high"},
	"1 The Conduit": {"base": "The Conduit", "class": "Divination Card", "type": "divination low"},
	"1 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"1 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"1 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination high"},
	"1 The Darkest Dream": {"base": "The Darkest Dream", "class": "Divination Card", "type": "divination high"},
	"1 The Deceiver": {"base": "The Deceiver", "class": "Divination Card", "type": "divination low"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination high"},
	"1 The Dreamer": {"base": "The Dreamer", "class": "Divination Card", "type": "divination very high"},
	"1 The Endless Darkness": {"base": "The Endless Darkness", "class": "Divination Card", "type": "divination very high"},
	"1 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"1 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"1 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination high"},
	"1 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination low"},
	"1 The Fiend": {"base": "The Fiend", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination high"},
	"1 The Gentleman": {"base": "The Gentleman", "class": "Divination Card", "type": "divination low"},
	"1 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"1 The Hale Heart": {"base": "The Hale Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination high"},
	"1 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Immortal": {"base": "The Immortal", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"1 The Innocent": {"base": "The Innocent", "class": "Divination Card", "type": "divination high"},
	"1 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"1 The Iron Bard": {"base": "The Iron Bard", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Jester": {"base": "The Jester", "class": "Divination Card", "type": "hide"},
	"1 The Jeweller's Boon": {"base": "The Jeweller's Boon", "class": "Divination Card", "type": "divination high"},
	"1 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Lord in Black": {"base": "The Lord in Black", "class": "Divination Card", "type": "hide"},
	"1 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination low"},
	"1 The Master": {"base": "The Master", "class": "Divination Card", "type": "divination very high"},
	"1 The Mayor": {"base": "The Mayor", "class": "Divination Card", "type": "divination very high"},
	"1 The Metalsmith's Gift": {"base": "The Metalsmith's Gift", "class": "Divination Card", "type": "hide"},
	"1 The Nurse": {"base": "The Nurse", "class": "Divination Card", "type": "divination very high"},
	"1 The Obscured": {"base": "The Obscured", "class": "Divination Card", "type": "divination high"},
	"1 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"1 The Opulent": {"base": "The Opulent", "class": "Divination Card", "type": "divination low"},
	"1 The Polymath": {"base": "The Polymath", "class": "Divination Card", "type": "divination very high"},
	"1 The Porcupine": {"base": "The Porcupine", "class": "Divination Card", "type": "divination high"},
	"1 The Price of Protection": {"base": "The Price of Protection", "class": "Divination Card", "type": "divination very high"},
	"1 The Professor": {"base": "The Professor", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination extremely high"},
	"1 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "hide"},
	"1 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"1 The Road to Power": {"base": "The Road to Power", "class": "Divination Card", "type": "hide"},
	"1 The Ruthless Ceinture": {"base": "The Ruthless Ceinture", "class": "Divination Card", "type": "divination low"},
	"1 The Sacrifice": {"base": "The Sacrifice", "class": "Divination Card", "type": "divination very high"},
	"1 The Saint's Treasure": {"base": "The Saint's Treasure", "class": "Divination Card", "type": "divination very high"},
	"1 The Samurai's Eye": {"base": "The Samurai's Eye", "class": "Divination Card", "type": "divination very high"},
	"1 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "hide"},
	"1 The Scavenger": {"base": "The Scavenger", "class": "Divination Card", "type": "divination high"},
	"1 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"1 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination high"},
	"1 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "hide"},
	"1 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination low"},
	"1 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination high"},
	"1 The Spark and the Flame": {"base": "The Spark and the Flame", "class": "Divination Card", "type": "divination very high"},
	"1 The Spoiled Prince": {"base": "The Spoiled Prince", "class": "Divination Card", "type": "hide"},
	"1 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "hide"},
	"1 The Sword King's Salute": {"base": "The Sword King's Salute", "class": "Divination Card", "type": "divination high"},
	"1 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"1 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination very high"},
	"1 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"1 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"1 The Twilight Moon": {"base": "The Twilight Moon", "class": "Divination Card", "type": "divination high"},
	"1 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "hide"},
	"1 The Tyrant": {"base": "The Tyrant", "class": "Divination Card", "type": "hide"},
	"1 The Undaunted": {"base": "The Undaunted", "class": "Divination Card", "type": "divination very high"},
	"1 The Undisputed": {"base": "The Undisputed", "class": "Divination Card", "type": "hide"},
	"1 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"1 The Vast": {"base": "The Vast", "class": "Divination Card", "type": "divination very high"},
	"1 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"1 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination high"},
	"1 The Web": {"base": "The Web", "class": "Divination Card", "type": "hide"},
	"1 The Wilted Rose": {"base": "The Wilted Rose", "class": "Divination Card", "type": "divination high"},
	"1 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination high"},
	"1 The Wolven King's Bite": {"base": "The Wolven King's Bite", "class": "Divination Card", "type": "divination very high"},
	"1 The World Eater": {"base": "The World Eater", "class": "Divination Card", "type": "divination very high"},
	"1 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "hide"},
	"1 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination very high"},
	"1 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "divination low"},
	"1 Wealth and Power": {"base": "Wealth and Power", "class": "Divination Card", "type": "divination very high"},
	"9 Other Divination Cards": {"class": "Divination Card", "type": "divination normal"}
}
