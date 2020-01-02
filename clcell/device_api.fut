-- This file is part of clcell which is released under MIT.
-- See file LICENSE for full license details.

-- Perform a single step of a cellular automaton.
let step [n] [m] (ruleset: [18]i32) (game_state: [n][m]i32): [n][m]i32 =
	-- Precompute last indicies before tabulation.
	let ni: i32 = n - 1
	let mi: i32 = m - 1
	in tabulate_2d n m (\(y: i32) (x: i32): i32 ->
		let is_interior_cell: bool = and [y>0,y<ni,x>0,x<mi]
		in if is_interior_cell then
			unsafe(ruleset[ -- Indexing into ruleset LUT is considered unsafe.
				game_state[y-1,x-1] + game_state[y-1,x] + game_state[y-1,x+1] +
				game_state[y,x-1] + game_state[y,x]*9 + game_state[y,x+1] +
				game_state[y+1,x-1] + game_state[y+1,x] + game_state[y+1,x+1]
			])
		else
			0 -- Force boundary cells to be unpopulated.
	)

-- Simulate a certain number of steps of a cellular automaton
-- using a seed state, and return the game state after the last step.
entry simulate [n] [m]
	(ruleset: [18]i32)
	(num_steps: i32)
	(seed_state: [n][m]i32): [n][m]i32 =
	loop game_state = seed_state for i < num_steps do step ruleset game_state

-- Simulate multiple cellular automata in parallel.
entry batch_simulate [l] [n] [m]
	(ruleset: [18]i32)
	(num_steps: i32)
	(seed_states: [l][n][m]i32): [l][m][n]i32 =
	let steps: [l]i32 = replicate l num_steps
	let rulesets: [l][18]i32 = map (\_ -> ruleset) steps
	in map3 simulate rulesets steps seed_states
