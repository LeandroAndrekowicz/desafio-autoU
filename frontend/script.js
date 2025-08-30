document.getElementById("emailForm").addEventListener("submit", handleFormSubmit);

async function handleFormSubmit(e) {
  e.preventDefault();

  resetUI();

  const formData = buildFormData();
  if (!formData) return;

  try {
    const data = await sendRequest(formData);
    handleResponse(data);
  } catch (err) {
    console.error(err);
    alert("Error processing email.");
  } finally {
    hideLoading();
  }
}

function resetUI() {
  const loadingEl = document.getElementById("loading");
  const resultEl = document.getElementById("result");
  const categoryEl = document.getElementById("categoria");
  const responseEl = document.getElementById("resposta");

  loadingEl.classList.remove("hidden");
  resultEl.classList.add("hidden");
  categoryEl.textContent = "";
  responseEl.textContent = "";
}

function buildFormData() {
  const formData = new FormData();
  const text = document.getElementById("text").value;
  const file = document.getElementById("file").files[0];

  if (file) {
    formData.append("file", file);
  } else if (text.trim() !== "") {
    formData.append("text", text);
  } else {
    alert("Please enter text or upload a file!");
    document.getElementById("resposta")
    return null;
  }

  return formData;
}

async function sendRequest(formData) {
  const response = await fetch(`${API_BASE_URL}/process`, {
    method: "POST",
    body: formData
  });

  return await response.json();
}

function handleResponse(data) {
  if (data.error) {
    alert(data.error);
    return;
  }

  document.getElementById("categoria").textContent = data.categoria;
  document.getElementById("resposta").textContent = data.resposta;
  document.getElementById("sugerida-por").textContent = data.sugeridoPor;

  document.getElementById("result").classList.remove("hidden");
}

function hideLoading() {
  document.getElementById("loading").classList.add("hidden");
}
