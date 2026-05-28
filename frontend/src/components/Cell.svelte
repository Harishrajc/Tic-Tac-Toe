<script>
  export let value = "";

  export let onClick;
</script>

<button
  class="cell"
  class:value-x={value === "X"}
  class:value-o={value === "O"}
  on:click={onClick}
>
  {value}
</button>

<style>

  .cell {

    width: 110px;
    height: 110px;

    border: none;

    border-radius: 15px;

    background: #374151;

    color: white;

    font-size: 3rem;

    font-weight: bold;

    cursor: pointer;

    transition: all 0.2s ease;
  }

  .cell:hover {

    background: #4b5563;

    transform: scale(1.05);
  }

  .cell:active {

    transform: scale(0.95);
  }

  .value-x {
    color: #60a5fa;
  }

  .value-o {
    color: #f87171;
  }

</style>