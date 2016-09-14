class Buff(object):
	def __init__(self, time, defence=0, damage_plus=0, mana_damage_plus=0, heal=0, damage=0, charisma=0, gold_bonus=1):
		super(Buff, self).__init__()
		self.time = time
		self.defence = defence
		self.damage_plus = damage_plus
		self.mana_damage_plus = mana_damage_plus
		self.heal = heal
		self.damage = damage
		self.charisma = charisma
		self.gold_bonus = gold_bonus

	def on_room(self, user, reply, room):
		self.time -= 1

	def on_end(self, user, reply, room):
		pass
		
class RainbowBuff(Buff):
	def __init__(self):
		super(RainbowBuff, self).__init__(50, mana_damage_plus=50)
		