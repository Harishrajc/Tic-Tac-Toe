<script>
  import Board from './components/Board.svelte'
</script>

<div class="app">
  
  <h1>Tic Tac Toe</h1>
  
  <Board />

</div>

<style>
  
  .app{
    min-height: 100vh;

    display: flex;
    flex-direction: column;

    justify-content: center;
    align-items: center;

    background: #111827;
    colour: white;

    font-family: Arial,sans-serif;
  }
  h1 {
    font-size:3rem;

    margin-bottom: 20px;

    color: #60a5fa;
  }
</style>