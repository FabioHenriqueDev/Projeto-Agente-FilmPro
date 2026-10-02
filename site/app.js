const form = document.querySelector("#recommendation-form");
const input = document.querySelector("#preferences");
const count = document.querySelector("#character-count");
const submitButton = document.querySelector("#submit-button");
const buttonLabel = document.querySelector("#button-label");
const feedback = document.querySelector("#feedback");
const resultsSection = document.querySelector("#results-section");
const movieGrid = document.querySelector("#movie-grid");
const resultsCount = document.querySelector("#results-count");
const apiStatus = document.querySelector("#api-status");
const apiStatusLabel = document.querySelector("#api-status-label");

async function refreshApiStatus() {
  try {
    const response = await fetch("/health", { cache: "no-store" });
    if (!response.ok) throw new Error("API indisponível");
    const health = await response.json();
    if (health.status !== "ok") throw new Error("API indisponível");
    apiStatus.className = "topbar-right api-online";
    apiStatusLabel.textContent = "API online · Seu próximo filme está por aqui";
    apiStatus.title = "API disponível";
  } catch {
    apiStatus.className = "topbar-right api-offline";
    apiStatusLabel.textContent = "API offline · tente novamente em instantes";
    apiStatus.title = "API indisponível";
  }
}

refreshApiStatus();
window.setInterval(refreshApiStatus, 15000);

input.addEventListener("input", () => { count.textContent = `${input.value.length} / 500`; });
document.querySelectorAll(".suggestion").forEach((button) => {
  button.addEventListener("click", () => { input.value = button.dataset.prompt; input.dispatchEvent(new Event("input")); input.focus(); });
});

function makeElement(tag, className, text) {
  const element = document.createElement(tag);
  if (className) element.className = className;
  if (text !== undefined && text !== null) element.textContent = text;
  return element;
}

function createMovieCard(movie, index) {
  const card = makeElement("article", "movie-card");
  card.style.animationDelay = `${Math.min(index * 70, 420)}ms`;
  const poster = makeElement("div", "poster");
  const monogram = (movie.title || "FP").split(/\s+/).slice(0, 2).map((part) => part[0]).join("").toUpperCase();
  poster.append(makeElement("span", "poster-monogram", monogram));
  if (movie.poster_url) {
    const image = document.createElement("img");
    image.src = movie.poster_url;
    image.alt = `Pôster de ${movie.title}`;
    image.loading = "lazy";
    image.onerror = () => image.remove();
    poster.prepend(image);
  }
  if (movie.imdb_rating !== undefined && movie.imdb_rating !== null) {
    const rating = makeElement("span", "rating");
    rating.append(makeElement("b", "", "★"), document.createTextNode(` ${movie.imdb_rating}`));
    poster.append(rating);
  }
  card.append(poster);
  const content = makeElement("div", "movie-content");
  const meta = [movie.release_year, movie.duration_minutes ? `${movie.duration_minutes} min` : null, movie.director].filter(Boolean).join(" · ");
  content.append(makeElement("div", "movie-meta", meta));
  content.append(makeElement("h3", "", movie.title || "Filme recomendado"));
  if (movie.synopsis) content.append(makeElement("p", "synopsis", movie.synopsis));
  if (Array.isArray(movie.genres) && movie.genres.length) {
    const tags = makeElement("div", "movie-extra");
    movie.genres.slice(0, 3).forEach((genre) => tags.append(makeElement("span", "tag", genre)));
    content.append(tags);
  }
  if (movie.recommendation_reason) {
    const reason = makeElement("p", "reason");
    reason.append(makeElement("strong", "", "Por que combina: "), document.createTextNode(movie.recommendation_reason));
    content.append(reason);
  }
  card.append(content);
  return card;
}

form.addEventListener("submit", async (event) => {
  event.preventDefault();
  const preferences = input.value.trim();
  if (preferences.length < 10) { feedback.textContent = "Conte um pouco mais: escreva pelo menos 10 caracteres."; input.focus(); return; }
  submitButton.disabled = true;
  buttonLabel.textContent = "Buscando recomendações…";
  feedback.textContent = "Estamos preparando uma seleção especial para você.";
  resultsSection.hidden = true;
  try {
    const response = await fetch("/recomendations", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ preferences }),
    });
    const payload = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(payload.detail || `A API respondeu com erro (${response.status}).`);
    const movies = payload.data?.movies;
    if (!Array.isArray(movies) || movies.length === 0) throw new Error("A API não retornou filmes. Tente descrever suas preferências de outro jeito.");
    movieGrid.replaceChildren(...movies.map(createMovieCard));
    resultsCount.textContent = `${movies.length} ${movies.length === 1 ? "filme" : "filmes"}`;
    resultsSection.hidden = false;
    feedback.textContent = "";
    resultsSection.scrollIntoView({ behavior: "smooth", block: "start" });
  } catch (error) {
    feedback.textContent = error.message || "Não foi possível conectar à API. Tente novamente.";
  } finally {
    submitButton.disabled = false;
    buttonLabel.textContent = "Encontrar meus filmes";
  }
});
