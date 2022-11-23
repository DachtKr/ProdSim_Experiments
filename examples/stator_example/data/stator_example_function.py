import random

# ---- process models ----
def apply_glue(env, item, machine, factory):
	yield env.timeout(1)


def dry_glue(env, item, machine, factory):
	yield env.timeout(1)


def weld_connections(env, item, machine, factory):

	machine.a_voltage_V = random.normalvariate(1.48, 0.23)
	machine.b_max_voltage_V = random.normalvariate(2.21, 0.15)
	machine.c_current_A = random.normalvariate(3657, 124)
	machine.d_resistance_mOhm = random.normalvariate(452, 1)
	machine.e_welding_energy_Ws = random.normalvariate(3312, 0.23)
	machine.f_force_one_N = random.normalvariate(184, 7.28)
	machine.g_force_two_N = random.normalvariate(186, 8.12)
	machine.h_movement_one_um = random.normalvariate(424, 11.49)
	machine.i_movement_two_um = random.normalvariate(422, 12.38)
	machine.j_welding_time_ms = random.normalvariate(813, 51.34)

	item.el_resistance_mOhm = machine.d_resistance_mOhm
	item.el_resistance_mOhm += machine.k_wear**2 * 1.5 - 2

	if item.el_resistance_mOhm >= 500:
		machine.k_wear = 0
		yield env.timeout(10)

	# it's possible to use the machine 50 times, before it has to be maintained
	machine.k_wear += 0.06

	yield env.timeout(1)


def check_quality(env, item, machine, factory):
	yield env.timeout(1)


def assemble_stator(env, item, machine, factory):
	yield env.timeout(1)


# ---- sources and sinks ---- 
def preassembly(env, factory):
	yield env.timeout(1)
	yield 1


def stator_source(env, factory):
	yield env.timeout(1)
	yield 2


# ---- global functions ---- 
def temperature_func(env, factory):
	yield env.timeout(1)


