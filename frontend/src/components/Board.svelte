<script>
  import Cell from './Cell.svelte';

import {
  makeMove,
  resetGame as resetApiGame,
  setDifficulty
} from "../services/api";

  let board = Array(9).fill("");

  let currentPlayer = "X";

  let winner = "";

  let draw = false;

  let xScore = 0;
  let oScore = 0;
  let drawScore = 0;

  let selectedDifficulty = "hard";

  async function handleClick(index) {

    const data = await makeMove(index);

    if (data.error) {
      alert(data.error);
      return;
    }

    board = data.board;

    currentPlayer = data.current_player;

    winner = data.winner;

    draw = data.draw;
    xScore = data.x_score;
    oScore = data.o_score;
    drawScore = data.draw_score;
  }

  async function changeDifficulty(event) {
    
    selectedDifficulty = event.target.value;

    await setDifficulty(selectedDifficulty);

    resetGame();
  }

  async function resetGame() {

    await resetApiGame();

    board = Array(9).fill("");

    currentPlayer = "X";

    winner = "";

    draw = false;
  }
</script>

<h2 class="player-info">
  You are X • Computer is O
</h2>

<div class="difficulty-container">

  <label for="difficulty">
  Difficulty:
</label>

  <select
  id="difficulty"
    bind:value={selectedDifficulty}
    on:change={changeDifficulty}
  >
    <option value="easy">
      Easy
    </option>

    <option value="medium">
      Medium
    </option>

    <option value="hard">
      Hard
    </option>

  </select>

</div>

<div class="scoreboard">

  <div class="score x-score">
    X : {xScore}
  </div>

  <div class="score o-score">
    O : {oScore}
  </div>

  <div class="score draw-score">
    Draws : {drawScore}
  </div>

</div>

{#if winner}
  <h2 class="winner">
    Winner: {winner}
  </h2>
{/if}

{#if draw}
  <h2 class="draw">
    It's a Draw!
  </h2>
{/if}

<div class="board">

  {#each board as cell, index}

    <Cell
      value={cell}
      onClick={() => handleClick(index)}
    />

  {/each}

</div>

<button
  class="reset-btn"
  on:click={resetGame}
>
  Reset Game
</button>

<style>

  .board {

    display: grid;

    grid-template-columns: repeat(3, 110px);

    gap: 10px;

    background: #1f2937;

    padding: 20px;

    border-radius: 20px;

    box-shadow:
      0 0 20px rgba(0,0,0,0.5);

    margin-top: 20px;
  }

  h2 {

    text-align: center;

    margin: 10px 0;

    color: white;
  }
   
  .difficulty-container {

  margin-bottom: 20px;

  display: flex;

  gap: 10px;

  align-items: center;

  color: white;
}

select {

  padding: 8px 12px;

  border-radius: 8px;

  border: none;

  background: #374151;

  color: white;

  cursor: pointer;
}

  .winner {

    color: #34d399;

    font-size: 2rem;

    animation: pop 0.4s ease;
  }
   
  .player-info {

  color: #cbd5e1;

  margin-bottom: 10px;

  text-align: center;
}

  .draw {

  color: #fbbf24;

  font-size: 2rem;

  margin-top: 10px;
}
  
  .scoreboard {

  display: flex;

  gap: 20px;

  margin-bottom: 20px;

  justify-content: center;

  flex-wrap: wrap;
}

.score {

  padding: 10px 20px;

  border-radius: 10px;

  font-weight: bold;

  font-size: 1.2rem;
}

.x-score {

  background: #1e3a8a;

  color: #93c5fd;
}

.o-score {

  background: #7f1d1d;

  color: #fca5a5;
}

.draw-score {

  background: #78350f;

  color: #fde68a;
}

  .reset-btn {

    margin-top: 20px;

    padding: 12px 24px;

    border: none;

    border-radius: 10px;

    background: #2563eb;

    color: white;

    font-size: 1rem;

    cursor: pointer;

    transition: 0.2s;
  }

  .reset-btn:hover {

    background: #1d4ed8;

    transform: translateY(-2px);
  }

  @keyframes pop {

    0% {
      transform: scale(0.5);
      opacity: 0;
    }

    100% {
      transform: scale(1);
      opacity: 1;
    }
  }

  @media (max-width: 500px) {

    .board {
      grid-template-columns: repeat(3, 90px);
    }
  }

</style>