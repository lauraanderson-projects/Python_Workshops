document.getElementById("generate-btn").addEventListener("click", async () => {
  const length = document.getElementById("length").value;
  const useUpper = document.getElementById("uppercase").checked;
  const useLower = document.getElementById("lowercase").checked;
  const useNumbers = document.getElementById("numbers").checked;
  const useSymbols = document.getElementById("symbols").checked;

  const response = await fetch("http://127.0.0.1:5000/generate-password", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      length: length,
      use_upper: useUpper,
      use_lower: useLower,
      use_numbers: useNumbers,
      use_symbols: useSymbols,
    }),
  });

  const data = await response.json();
  document.getElementById("password").value = data.password;
});
