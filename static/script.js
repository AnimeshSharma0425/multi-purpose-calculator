const INVALID_CHOICE = "Invalid choice! Please enter a number from 1 to 18";

const menuEl = document.getElementById("menu");
const conditionForm = document.getElementById("condition-form");
const conditionInput = document.getElementById("condition");
const valuesForm = document.getElementById("values-form");
const opName = document.getElementById("op-name");
const fields = document.getElementById("fields");
const message = document.getElementById("message");
const resultBox = document.getElementById("result");
const resultValue = document.getElementById("result-value");

let operations = [];
let current = null; // the option chosen in step 1

function showMessage(text, isError = false) {
  message.textContent = text;
  message.classList.toggle("error", isError);
}

function clearOutput() {
  showMessage("");
  resultBox.classList.add("hidden");
}

function resetToMenu() {
  valuesForm.classList.add("hidden");
  fields.innerHTML = "";
  current = null;
  conditionInput.value = "";
  conditionInput.focus();
}

async function loadOperations() {
  try {
    const res = await fetch("/api/operations");
    const data = await res.json();
    operations = data.operations;
    operations.forEach((op) => {
      const li = document.createElement("li");
      li.textContent = op.name;
      menuEl.appendChild(li);
    });
  } catch {
    showMessage("Could not reach the server", true);
  }
}

// Step 1: the condition number, same as the console menu
conditionForm.addEventListener("submit", (e) => {
  e.preventDefault();
  clearOutput();
  valuesForm.classList.add("hidden");

  const id = Number(conditionInput.value);
  const op = operations.find((o) => o.id === id);

  if (!op) {
    showMessage(INVALID_CHOICE, true);
    return;
  }

  if (op.exit) {
    showMessage("Thank you for using Multi-Purpose Calculator!");
    conditionInput.disabled = true;
    conditionForm.querySelector("button").disabled = true;
    return;
  }

  // Step 2: ask only for the inputs this option needs
  current = op;
  opName.textContent = op.name;
  fields.innerHTML = "";
  op.inputs.forEach((label, i) => {
    const wrap = document.createElement("div");
    wrap.className = "field";

    const lab = document.createElement("label");
    lab.htmlFor = "value-" + i;
    lab.textContent = label + ":";

    const input = document.createElement("input");
    input.id = "value-" + i;
    input.type = "number";
    input.step = "any";
    input.required = true;

    wrap.append(lab, input);
    fields.appendChild(wrap);
  });
  valuesForm.classList.remove("hidden");
  fields.querySelector("input").focus();
});

// Step 3: send the values to the FastAPI backend
valuesForm.addEventListener("submit", async (e) => {
  e.preventDefault();
  if (!current) return;
  clearOutput();

  const values = [...fields.querySelectorAll("input")].map((i) => parseFloat(i.value));
  if (values.some(Number.isNaN)) {
    showMessage("Please enter valid numbers", true);
    return;
  }

  try {
    const res = await fetch("/api/calculate", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ condition: current.id, values }),
    });
    const data = await res.json().catch(() => ({}));

    if (!res.ok) {
      showMessage(typeof data.detail === "string" ? data.detail : "Please check your inputs", true);
      return;
    }

    resultValue.textContent = data.result;
    resultBox.classList.remove("hidden");
    resetToMenu(); // like the console loop: back to the menu for the next calculation
  } catch {
    showMessage("Could not reach the server. Please try again.", true);
  }
});

loadOperations();
