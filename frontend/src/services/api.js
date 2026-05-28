const API_URL = "http://127.0.0.1:8000";

export async function makeMove(position) {

  const response = await fetch(
    `${API_URL}/move`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        position
      })
    }
  );

  return await response.json();
}

export async function setDifficulty(difficulty) {

  const response = await fetch(
    `${API_URL}/difficulty`,
    {
      method: "POST",

      headers: {
        "Content-Type": "application/json"
      },

      body: JSON.stringify({
        difficulty
      })
    }
  );

  return await response.json();
}

export async function resetGame() {

  const response = await fetch(
    `${API_URL}/reset`,
    {
      method: "POST"
    }
  );

  return await response.json();
}