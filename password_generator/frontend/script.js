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

function copyToClipboard(event) {
  event.preventDefault(); // Prevent form submission (if applicable)

  const passwordField = document.getElementById("password");

  // Use modern clipboard API for better performance
  navigator.clipboard
    .writeText(passwordField.value)
    .then(() => {
      // Show a temporary success message
      const copyButton = document.getElementById("copy-btn");
      copyButton.textContent = "Copied!";
      copyButton.style.backgroundColor = "#4CAF50"; // Green feedback

      setTimeout(() => {
        copyButton.textContent = "Copy";
        copyButton.style.backgroundColor = ""; // Reset after 2 seconds
      }, 2000);
    })
    .catch((err) => {
      console.error("Failed to copy:", err);
      alert("Failed to copy password.");
    });
}
