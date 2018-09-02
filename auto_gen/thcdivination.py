#!/usr/bin/python
# -*- coding: utf-8 -*-
# Created: 09/02/2018(m/d/y) 17:46:10 UTC from "tmphardcore" data

desc = "Divination Card"

# Base type : settings pair
items = {
	"000 The Wolf's Shadow": {"base": "The Wolf's Shadow", "class": "Divination Card", "type": "divination high"},
	"001 The Dragon's Heart": {"base": "The Dragon's Heart", "class": "Divination Card", "type": "divination very high"},
	"002 Last Hope": {"base": "Last Hope", "class": "Divination Card", "type": "divination high"},
	"003 Glimmer of Hope": {"base": "Glimmer of Hope", "class": "Divination Card", "type": "divination high"},
	"004 Beauty Through Death": {"base": "Beauty Through Death", "class": "Divination Card", "type": "divination very high"},
	"1 Abandoned Wealth": {"base": "Abandoned Wealth", "class": "Divination Card", "type": "divination very high"},
	"1 Blind Venture": {"base": "Blind Venture", "class": "Divination Card", "type": "divination very high"},
	"1 Boon of the First Ones": {"base": "Boon of the First Ones", "class": "Divination Card", "type": "divination very high"},
	"1 Emperor of Purity": {"base": "Emperor of Purity", "class": "Divination Card", "type": "divination very high"},
	"1 Heterochromia": {"base": "Heterochromia", "class": "Divination Card", "type": "divination very high"},
	"1 House of Mirrors": {"base": "House of Mirrors", "class": "Divination Card", "type": "divination very high"},
	"1 Hunter's Reward": {"base": "Hunter's Reward", "class": "Divination Card", "type": "divination very high"},
	"1 Left to Fate": {"base": "Left to Fate", "class": "Divination Card", "type": "divination very high"},
	"1 Lucky Deck": {"base": "Lucky Deck", "class": "Divination Card", "type": "divination very high"},
	"1 Pride Before the Fall": {"base": "Pride Before the Fall", "class": "Divination Card", "type": "divination very high"},
	"1 The Brittle Emperor": {"base": "The Brittle Emperor", "class": "Divination Card", "type": "divination very high"},
	"1 The Celestial Justicar": {"base": "The Celestial Justicar", "class": "Divination Card", "type": "divination very high"},
	"1 The Dapper Prodigy": {"base": "The Dapper Prodigy", "class": "Divination Card", "type": "divination very high"},
	"1 The Dark Mage": {"base": "The Dark Mage", "class": "Divination Card", "type": "divination very high"},
	"1 The Doctor": {"base": "The Doctor", "class": "Divination Card", "type": "divination very high"},
	"1 The Dreamer": {"base": "The Dreamer", "class": "Divination Card", "type": "divination very high"},
	"1 The Endless Darkness": {"base": "The Endless Darkness", "class": "Divination Card", "type": "divination very high"},
	"1 The Enlightened": {"base": "The Enlightened", "class": "Divination Card", "type": "divination very high"},
	"1 The Ethereal": {"base": "The Ethereal", "class": "Divination Card", "type": "divination very high"},
	"1 The Formless Sea": {"base": "The Formless Sea", "class": "Divination Card", "type": "divination very high"},
	"1 The Hunger": {"base": "The Hunger", "class": "Divination Card", "type": "divination very high"},
	"1 The Iron Bard": {"base": "The Iron Bard", "class": "Divination Card", "type": "divination very high"},
	"1 The King's Heart": {"base": "The King's Heart", "class": "Divination Card", "type": "divination very high"},
	"1 The Last One Standing": {"base": "The Last One Standing", "class": "Divination Card", "type": "divination very high"},
	"1 The Master": {"base": "The Master", "class": "Divination Card", "type": "divination very high"},
	"1 The Offering": {"base": "The Offering", "class": "Divination Card", "type": "divination very high"},
	"1 The Polymath": {"base": "The Polymath", "class": "Divination Card", "type": "divination very high"},
	"1 The Porcupine": {"base": "The Porcupine", "class": "Divination Card", "type": "divination very high"},
	"1 The Price of Protection": {"base": "The Price of Protection", "class": "Divination Card", "type": "divination very high"},
	"1 The Professor": {"base": "The Professor", "class": "Divination Card", "type": "divination very high"},
	"1 The Queen": {"base": "The Queen", "class": "Divination Card", "type": "divination very high"},
	"1 The Samurai's Eye": {"base": "The Samurai's Eye", "class": "Divination Card", "type": "divination very high"},
	"1 The Soul": {"base": "The Soul", "class": "Divination Card", "type": "divination very high"},
	"1 The Spark and the Flame": {"base": "The Spark and the Flame", "class": "Divination Card", "type": "divination very high"},
	"1 The Thaumaturgist": {"base": "The Thaumaturgist", "class": "Divination Card", "type": "divination very high"},
	"1 The Throne": {"base": "The Throne", "class": "Divination Card", "type": "divination very high"},
	"1 The Wind": {"base": "The Wind", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolf": {"base": "The Wolf", "class": "Divination Card", "type": "divination very high"},
	"1 The Wolven King's Bite": {"base": "The Wolven King's Bite", "class": "Divination Card", "type": "divination very high"},
	"1 The World Eater": {"base": "The World Eater", "class": "Divination Card", "type": "divination very high"},
	"2 A Mother's Parting Gift": {"base": "A Mother's Parting Gift", "class": "Divination Card", "type": "divination high"},
	"2 Anarchy's Price": {"base": "Anarchy's Price", "class": "Divination Card", "type": "divination high"},
	"2 Assassin's Favour": {"base": "Assassin's Favour", "class": "Divination Card", "type": "divination high"},
	"2 Atziri's Arsenal": {"base": "Atziri's Arsenal", "class": "Divination Card", "type": "divination high"},
	"2 Audacity": {"base": "Audacity", "class": "Divination Card", "type": "divination high"},
	"2 Boundless Realms": {"base": "Boundless Realms", "class": "Divination Card", "type": "divination high"},
	"2 Bowyer's Dream": {"base": "Bowyer's Dream", "class": "Divination Card", "type": "divination high"},
	"2 Cartographer's Delight": {"base": "Cartographer's Delight", "class": "Divination Card", "type": "divination high"},
	"2 Coveted Possession": {"base": "Coveted Possession", "class": "Divination Card", "type": "divination high"},
	"2 Death": {"base": "Death", "class": "Divination Card", "type": "divination high"},
	"2 Dialla's Subjugation": {"base": "Dialla's Subjugation", "class": "Divination Card", "type": "divination high"},
	"2 Dying Anguish": {"base": "Dying Anguish", "class": "Divination Card", "type": "divination high"},
	"2 Earth Drinker": {"base": "Earth Drinker", "class": "Divination Card", "type": "divination high"},
	"2 Emperor's Luck": {"base": "Emperor's Luck", "class": "Divination Card", "type": "divination high"},
	"2 Forbidden Power": {"base": "Forbidden Power", "class": "Divination Card", "type": "divination high"},
	"2 Gemcutter's Promise": {"base": "Gemcutter's Promise", "class": "Divination Card", "type": "divination high"},
	"2 Gift of the Gemling Queen": {"base": "Gift of the Gemling Queen", "class": "Divination Card", "type": "divination high"},
	"2 Grave Knowledge": {"base": "Grave Knowledge", "class": "Divination Card", "type": "divination high"},
	"2 Her Mask": {"base": "Her Mask", "class": "Divination Card", "type": "divination high"},
	"2 Hope": {"base": "Hope", "class": "Divination Card", "type": "divination high"},
	"2 Hubris": {"base": "Hubris", "class": "Divination Card", "type": "divination high"},
	"2 Humility": {"base": "Humility", "class": "Divination Card", "type": "divination high"},
	"2 Hunter's Resolve": {"base": "Hunter's Resolve", "class": "Divination Card", "type": "divination high"},
	"2 Jack in the Box": {"base": "Jack in the Box", "class": "Divination Card", "type": "divination high"},
	"2 Light and Truth": {"base": "Light and Truth", "class": "Divination Card", "type": "divination high"},
	"2 Lost Worlds": {"base": "Lost Worlds", "class": "Divination Card", "type": "divination high"},
	"2 Loyalty": {"base": "Loyalty", "class": "Divination Card", "type": "divination high"},
	"2 Lucky Connections": {"base": "Lucky Connections", "class": "Divination Card", "type": "divination high"},
	"2 Might is Right": {"base": "Might is Right", "class": "Divination Card", "type": "divination high"},
	"2 Mitts": {"base": "Mitts", "class": "Divination Card", "type": "divination high"},
	"2 No Traces": {"base": "No Traces", "class": "Divination Card", "type": "divination high"},
	"2 Rain Tempter": {"base": "Rain Tempter", "class": "Divination Card", "type": "divination high"},
	"2 Rats": {"base": "Rats", "class": "Divination Card", "type": "divination high"},
	"2 Rebirth": {"base": "Rebirth", "class": "Divination Card", "type": "divination high"},
	"2 Scholar of the Seas": {"base": "Scholar of the Seas", "class": "Divination Card", "type": "divination high"},
	"2 The Admirer": {"base": "The Admirer", "class": "Divination Card", "type": "divination high"},
	"2 The Aesthete": {"base": "The Aesthete", "class": "Divination Card", "type": "divination high"},
	"2 The Avenger": {"base": "The Avenger", "class": "Divination Card", "type": "divination high"},
	"2 The Battle Born": {"base": "The Battle Born", "class": "Divination Card", "type": "divination high"},
	"2 The Beast": {"base": "The Beast", "class": "Divination Card", "type": "divination high"},
	"2 The Betrayal": {"base": "The Betrayal", "class": "Divination Card", "type": "divination high"},
	"2 The Blazing Fire": {"base": "The Blazing Fire", "class": "Divination Card", "type": "divination high"},
	"2 The Body": {"base": "The Body", "class": "Divination Card", "type": "divination high"},
	"2 The Breach": {"base": "The Breach", "class": "Divination Card", "type": "divination high"},
	"2 The Calling": {"base": "The Calling", "class": "Divination Card", "type": "divination high"},
	"2 The Cartographer": {"base": "The Cartographer", "class": "Divination Card", "type": "divination high"},
	"2 The Chains that Bind": {"base": "The Chains that Bind", "class": "Divination Card", "type": "divination high"},
	"2 The Coming Storm": {"base": "The Coming Storm", "class": "Divination Card", "type": "divination high"},
	"2 The Conduit": {"base": "The Conduit", "class": "Divination Card", "type": "divination high"},
	"2 The Cursed King": {"base": "The Cursed King", "class": "Divination Card", "type": "divination high"},
	"2 The Darkest Dream": {"base": "The Darkest Dream", "class": "Divination Card", "type": "divination high"},
	"2 The Demoness": {"base": "The Demoness", "class": "Divination Card", "type": "divination high"},
	"2 The Doppelganger": {"base": "The Doppelganger", "class": "Divination Card", "type": "divination high"},
	"2 The Dragon": {"base": "The Dragon", "class": "Divination Card", "type": "divination high"},
	"2 The Dreamland": {"base": "The Dreamland", "class": "Divination Card", "type": "divination high"},
	"2 The Encroaching Darkness": {"base": "The Encroaching Darkness", "class": "Divination Card", "type": "divination high"},
	"2 The Explorer": {"base": "The Explorer", "class": "Divination Card", "type": "divination high"},
	"2 The Eye of the Dragon": {"base": "The Eye of the Dragon", "class": "Divination Card", "type": "divination high"},
	"2 The Fathomless Depths": {"base": "The Fathomless Depths", "class": "Divination Card", "type": "divination high"},
	"2 The Feast": {"base": "The Feast", "class": "Divination Card", "type": "divination high"},
	"2 The Fletcher": {"base": "The Fletcher", "class": "Divination Card", "type": "divination high"},
	"2 The Fox": {"base": "The Fox", "class": "Divination Card", "type": "divination high"},
	"2 The Gambler": {"base": "The Gambler", "class": "Divination Card", "type": "divination high"},
	"2 The Garish Power": {"base": "The Garish Power", "class": "Divination Card", "type": "divination high"},
	"2 The Gladiator": {"base": "The Gladiator", "class": "Divination Card", "type": "divination high"},
	"2 The Harvester": {"base": "The Harvester", "class": "Divination Card", "type": "divination high"},
	"2 The Hoarder": {"base": "The Hoarder", "class": "Divination Card", "type": "divination high"},
	"2 The Innocent": {"base": "The Innocent", "class": "Divination Card", "type": "divination high"},
	"2 The Inventor": {"base": "The Inventor", "class": "Divination Card", "type": "divination high"},
	"2 The Jeweller's Boon": {"base": "The Jeweller's Boon", "class": "Divination Card", "type": "divination high"},
	"2 The Lion": {"base": "The Lion", "class": "Divination Card", "type": "divination high"},
	"2 The Lord in Black": {"base": "The Lord in Black", "class": "Divination Card", "type": "divination high"},
	"2 The Lover": {"base": "The Lover", "class": "Divination Card", "type": "divination high"},
	"2 The Lunaris Priestess": {"base": "The Lunaris Priestess", "class": "Divination Card", "type": "divination high"},
	"2 The Mayor": {"base": "The Mayor", "class": "Divination Card", "type": "divination high"},
	"2 The Mercenary": {"base": "The Mercenary", "class": "Divination Card", "type": "divination high"},
	"2 The Oath": {"base": "The Oath", "class": "Divination Card", "type": "divination high"},
	"2 The Obscured": {"base": "The Obscured", "class": "Divination Card", "type": "divination high"},
	"2 The One With All": {"base": "The One With All", "class": "Divination Card", "type": "divination high"},
	"2 The Opulent": {"base": "The Opulent", "class": "Divination Card", "type": "divination high"},
	"2 The Pack Leader": {"base": "The Pack Leader", "class": "Divination Card", "type": "divination high"},
	"2 The Penitent": {"base": "The Penitent", "class": "Divination Card", "type": "divination high"},
	"2 The Poet": {"base": "The Poet", "class": "Divination Card", "type": "divination high"},
	"2 The Puzzle": {"base": "The Puzzle", "class": "Divination Card", "type": "divination high"},
	"2 The Realm": {"base": "The Realm", "class": "Divination Card", "type": "divination high"},
	"2 The Risk": {"base": "The Risk", "class": "Divination Card", "type": "divination high"},
	"2 The Rite of Elements": {"base": "The Rite of Elements", "class": "Divination Card", "type": "divination high"},
	"2 The Ruthless Ceinture": {"base": "The Ruthless Ceinture", "class": "Divination Card", "type": "divination high"},
	"2 The Saint's Treasure": {"base": "The Saint's Treasure", "class": "Divination Card", "type": "divination high"},
	"2 The Scarred Meadow": {"base": "The Scarred Meadow", "class": "Divination Card", "type": "divination high"},
	"2 The Sephirot": {"base": "The Sephirot", "class": "Divination Card", "type": "divination high"},
	"2 The Siren": {"base": "The Siren", "class": "Divination Card", "type": "divination high"},
	"2 The Stormcaller": {"base": "The Stormcaller", "class": "Divination Card", "type": "divination high"},
	"2 The Summoner": {"base": "The Summoner", "class": "Divination Card", "type": "divination high"},
	"2 The Sun": {"base": "The Sun", "class": "Divination Card", "type": "divination high"},
	"2 The Surveyor": {"base": "The Surveyor", "class": "Divination Card", "type": "divination high"},
	"2 The Survivalist": {"base": "The Survivalist", "class": "Divination Card", "type": "divination high"},
	"2 The Sword King's Salute": {"base": "The Sword King's Salute", "class": "Divination Card", "type": "divination high"},
	"2 The Tower": {"base": "The Tower", "class": "Divination Card", "type": "divination high"},
	"2 The Traitor": {"base": "The Traitor", "class": "Divination Card", "type": "divination high"},
	"2 The Trial": {"base": "The Trial", "class": "Divination Card", "type": "divination high"},
	"2 The Twilight Moon": {"base": "The Twilight Moon", "class": "Divination Card", "type": "divination high"},
	"2 The Undaunted": {"base": "The Undaunted", "class": "Divination Card", "type": "divination high"},
	"2 The Union": {"base": "The Union", "class": "Divination Card", "type": "divination high"},
	"2 The Valkyrie": {"base": "The Valkyrie", "class": "Divination Card", "type": "divination high"},
	"2 The Valley of Steel Boxes": {"base": "The Valley of Steel Boxes", "class": "Divination Card", "type": "divination high"},
	"2 The Void": {"base": "The Void", "class": "Divination Card", "type": "divination high"},
	"2 The Warden": {"base": "The Warden", "class": "Divination Card", "type": "divination high"},
	"2 The Warlord": {"base": "The Warlord", "class": "Divination Card", "type": "divination high"},
	"2 The Watcher": {"base": "The Watcher", "class": "Divination Card", "type": "divination high"},
	"2 The Wilted Rose": {"base": "The Wilted Rose", "class": "Divination Card", "type": "divination high"},
	"2 The Wolverine": {"base": "The Wolverine", "class": "Divination Card", "type": "divination high"},
	"2 The Wretched": {"base": "The Wretched", "class": "Divination Card", "type": "divination high"},
	"2 Three Faces in the Dark": {"base": "Three Faces in the Dark", "class": "Divination Card", "type": "divination high"},
	"2 Time-Lost Relic": {"base": "Time-Lost Relic", "class": "Divination Card", "type": "divination high"},
	"2 Tranquillity": {"base": "Tranquillity", "class": "Divination Card", "type": "divination high"},
	"2 Treasure Hunter": {"base": "Treasure Hunter", "class": "Divination Card", "type": "divination high"},
	"2 Turn the Other Cheek": {"base": "Turn the Other Cheek", "class": "Divination Card", "type": "divination high"},
	"2 Vinia's Token": {"base": "Vinia's Token", "class": "Divination Card", "type": "divination high"},
	"3 Destined to Crumble": {"base": "Destined to Crumble", "class": "Divination Card", "type": "divination low"},
	"3 Doedre's Madness": {"base": "Doedre's Madness", "class": "Divination Card", "type": "divination low"},
	"3 Lantador's Lost Love": {"base": "Lantador's Lost Love", "class": "Divination Card", "type": "divination low"},
	"3 Shard of Fate": {"base": "Shard of Fate", "class": "Divination Card", "type": "divination low"},
	"3 The Drunken Aristocrat": {"base": "The Drunken Aristocrat", "class": "Divination Card", "type": "divination low"},
	"3 The Endurance": {"base": "The Endurance", "class": "Divination Card", "type": "divination low"},
	"3 The Incantation": {"base": "The Incantation", "class": "Divination Card", "type": "divination low"},
	"3 The Lich": {"base": "The Lich", "class": "Divination Card", "type": "divination low"},
	"3 The Rabid Rhoa": {"base": "The Rabid Rhoa", "class": "Divination Card", "type": "divination low"},
	"3 The Scholar": {"base": "The Scholar", "class": "Divination Card", "type": "divination low"},
	"3 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "divination low"},
	"3 The Twins": {"base": "The Twins", "class": "Divination Card", "type": "divination low"},
	"3 Thunderous Skies": {"base": "Thunderous Skies", "class": "Divination Card", "type": "divination low"},
	"7 Prosperity": {"base": "Prosperity", "class": "Divination Card", "type": "hide"},
	"7 Struck by Lightning": {"base": "Struck by Lightning", "class": "Divination Card", "type": "hide"},
	"7 The Carrion Crow": {"base": "The Carrion Crow", "class": "Divination Card", "type": "hide"},
	"7 The Inoculated": {"base": "The Inoculated", "class": "Divination Card", "type": "hide"},
	"7 The King's Blade": {"base": "The King's Blade", "class": "Divination Card", "type": "hide"},
	"7 The Sigil": {"base": "The Sigil", "class": "Divination Card", "type": "hide"},
	"7 The Surgeon": {"base": "The Surgeon", "class": "Divination Card", "type": "hide"},
	"7 The Web": {"base": "The Web", "class": "Divination Card", "type": "hide"},
	"9 Other uniques": {"class": "Divination Card", "type": "divination normal"}
}
