const QUESTIONS = [
  {
    tag: "Módulo 1 · Força magnética",
    q: "Uma carga elétrica se move exatamente na mesma direção das linhas de um campo magnético (ângulo θ = 0° entre v e B). O que acontece com a força magnética sobre ela?",
    options: [
      "É máxima, porque o campo está presente",
      "É zero, porque sen(0°) = 0",
      "Depende apenas da intensidade de B",
      "É sempre igual ao peso da partícula",
    ],
    correct: 1,
    explain: "F = q·v·B·sen(θ). Como sen(0°) = 0, a força é zero mesmo com campo e velocidade grandes. A força magnética só existe quando há uma componente de velocidade perpendicular ao campo.",
    example: "É como o nadador nadando a favor da correnteza do rio: ele não sente nenhum empurrão lateral, mesmo com a correnteza forte. Só sente o empurrão quando atravessa o rio (perpendicular a ele).",
  },
  {
    tag: "Módulo 2 · Fluxo magnético",
    q: "Uma espira está perpendicular a um campo magnético (ângulo entre B e a normal da espira = 0°). Se você girar a espira até ficar paralela às linhas de campo (ângulo = 90°), o que acontece com o fluxo magnético Φ?",
    options: [
      "Permanece o mesmo, pois B não mudou",
      "Dobra de valor",
      "Cai para zero, pois cos(90°) = 0",
      "Fica negativo e maior em módulo",
    ],
    correct: 2,
    explain: "Φ = B·A·cos(θ). Com θ = 90°, cos(90°) = 0, então Φ = 0, mesmo que B e a área A continuem exatamente os mesmos. O fluxo depende do ângulo, não só da intensidade do campo.",
    example: "É como inclinar um guarda-chuva de lado durante uma chuva forte: a chuva (B) continua igual, mas quase nenhuma água (fluxo) atravessa o guarda-chuva quando ele fica de perfil.",
  },
  {
    tag: "Módulo 3 · Lei de Faraday",
    q: "Um ímã permanece parado, bem no centro de uma espira de fio condutor, por vários minutos. Qual é a corrente induzida na espira durante esse tempo?",
    options: [
      "Máxima, pois o fluxo magnético ali é grande",
      "Zero, pois o fluxo não está variando",
      "Depende da cor do fio",
      "Alternada, com frequência igual à rede elétrica",
    ],
    correct: 1,
    explain: "A Lei de Faraday exige variação do fluxo no tempo (ΔΦ/Δt) para gerar f.e.m. Fluxo grande e constante gera ε = 0, porque ΔΦ = 0.",
    example: "Como a esponja encharcada parada na sua mão: por mais molhada que esteja, nenhuma água escorre até você apertar (mudar) alguma coisa.",
  },
  {
    tag: "Módulo 3 · Cálculo",
    q: "Uma bobina com N = 20 espiras, área total por espira A = 0,10 m², está perpendicular a um campo magnético que varia de 0 a 0,40 T em 0,2 s. Qual a f.e.m. induzida média?",
    options: [
      "ε = 0,4 V",
      "ε = 4,0 V",
      "ε = 40 V",
      "ε = 400 V",
    ],
    correct: 1,
    explain: "ΔΦ/Δt = A·(ΔB/Δt) = 0,10 × (0,40/0,2) = 0,10 × 2,0 = 0,2 Wb/s. ε = N·ΔΦ/Δt = 20 × 0,2 = 4,0 V.",
    example: "Mesmo raciocínio do exemplo da ressonância magnética no guia: calcule primeiro a taxa de variação do campo (ΔB/Δt), multiplique pela área para achar ΔΦ/Δt, e só depois multiplique por N.",
  },
  {
    tag: "Módulo 4 · Lei de Lenz",
    q: "Você aproxima o polo norte de um ímã de uma espira de fio. De acordo com a Lei de Lenz, o campo magnético criado pela corrente induzida na espira irá:",
    options: [
      "Atrair o ímã, facilitando sua aproximação",
      "Repelir o ímã, dificultando sua aproximação",
      "Ficar neutro, sem interagir com o ímã",
      "Inverter a polaridade do próprio ímã",
    ],
    correct: 1,
    explain: "A Lei de Lenz diz que a corrente induzida se opõe à variação do fluxo que a gerou. Como o fluxo está aumentando (ímã se aproximando), a espira cria um campo que repele o ímã, tentando frear a aproximação.",
    example: "Como o freio magnético de uma montanha-russa: a corrente induzida nos trilhos metálicos sempre se opõe ao movimento do carrinho, nunca o acelera.",
  },
  {
    tag: "Módulo 5 · Leitura de gráfico",
    q: "No gráfico de fluxo Φ por tempo t de uma bobina, um trecho é perfeitamente horizontal (Φ constante e diferente de zero) durante 2 segundos. Qual a f.e.m. induzida nesse trecho?",
    options: [
      "Máxima, pois o fluxo está no seu valor mais alto",
      "Proporcional ao valor de Φ nesse trecho",
      "Zero, pois a inclinação da reta é zero",
      "Impossível calcular sem saber a resistência do fio",
    ],
    correct: 2,
    explain: "ε é proporcional à inclinação (declividade) do gráfico Φ×t, não ao valor absoluto de Φ. Trecho plano = inclinação zero = f.e.m. zero, mesmo com fluxo grande.",
    example: "Como o velocímetro de um carro parado num sinal: o odômetro (equivalente ao fluxo acumulado) pode marcar um valor enorme, mas o velocímetro (equivalente à f.e.m.) marca zero porque não há variação naquele instante.",
  },
  {
    tag: "Módulo 6 · CA vs CC",
    q: "A base de um carregador de celular sem fio precisa induzir corrente continuamente, o tempo todo em que o celular está sobre ela. Por isso, a bobina da base é alimentada por:",
    options: [
      "Corrente contínua constante, pois é mais eficiente",
      "Corrente alternada, pois mantém o fluxo sempre variando",
      "Corrente contínua pulsada apenas uma vez, no início",
      "Nenhuma corrente — o campo é só do ímã do celular",
    ],
    correct: 1,
    explain: "Só a corrente alternada faz o fluxo subir e descer sem parar, o que mantém ΔΦ/Δt diferente de zero continuamente. Corrente contínua constante geraria apenas um pulso de indução no instante de ligar/desligar.",
    example: "É a diferença entre andar sempre reto (CC — sem variação depois do início) e ficar numa cadeira de balanço (CA — vaivém constante, que mantém tudo em movimento).",
  },
  {
    tag: "Módulo 7 · Aplicação",
    q: "Num fogão de indução, o vidro da superfície praticamente não esquenta, mas o fundo da panela metálica esquenta bastante. Isso acontece porque:",
    options: [
      "O vidro é isolante térmico perfeito",
      "A panela metálica funciona como uma espira onde o fluxo variável induz correntes que a aquecem por efeito Joule",
      "A bobina toca diretamente a panela, transferindo calor por condução",
      "O vidro bloqueia todo o campo magnético",
    ],
    correct: 1,
    explain: "A bobina sob o vidro gera um campo magnético alternado. O fundo da panela (metálico) se comporta como uma espira de fio: o fluxo variando dentro dela induz correntes elétricas, que aquecem o metal pela sua resistência (efeito Joule). O vidro não é condutor, então não sofre indução.",
    example: "É o mesmo princípio da bobina de ignição do carro e do carregador sem fio: um campo que varia induz corrente em qualquer condutor próximo — aqui, o condutor é o próprio fundo da panela.",
  },
  {
    tag: "Módulo 7 · Transformador",
    q: "No sistema de ignição automotivo, a bateria (12 V, baixa tensão) alimenta o enrolamento primário de uma bobina. Ao cortar essa corrente de forma abrupta, surge uma tensão muito alta no enrolamento secundário, suficiente para gerar a centelha na vela. Isso é um exemplo direto de:",
    options: [
      "Força de Lorentz sobre cargas livres",
      "Lei de Faraday, com ΔΦ/Δt muito grande por causa do corte abrupto de corrente",
      "Simples resistência elétrica do fio aquecendo",
      "Corrente contínua sendo multiplicada por um resistor",
    ],
    correct: 1,
    explain: "Cortar a corrente do primário rapidamente faz o fluxo magnético despencar quase instantaneamente (Δt muito pequeno), o que torna ΔΦ/Δt gigantesco — e por isso a tensão induzida no secundário é tão alta, mesmo partindo de apenas 12 V.",
    example: "É o mesmo efeito do solenoide de ressonância magnética do guia: quanto menor o Δt da variação, maior a f.e.m. induzida, mesmo com a mesma variação total de fluxo.",
  },
  {
    tag: "Revisão geral",
    q: "Qual frase resume melhor TODA a indução eletromagnética?",
    options: [
      "Corrente elétrica sempre existe onde há ímã por perto",
      "Parado não gera, só mudança cria — e a bobina sempre se vira contra quem mexeu nela",
      "Quanto maior o ímã, maior a corrente, não importa o movimento",
      "Só corrente contínua pode induzir outra corrente",
    ],
    correct: 1,
    explain: "Essa é exatamente a síntese da Lei de Faraday (só a VARIAÇÃO do fluxo gera f.e.m.) com a Lei de Lenz (a corrente induzida sempre se OPÕE à variação que a criou).",
    example: "Volte na história do 'Ímã Preguiçoso e da Bobina Birrenta' no guia de estudo sempre que precisar relembrar rápido esse conceito antes de uma prova.",
  },
];

let current = 0;
let answers = new Array(QUESTIONS.length).fill(null);

const root = document.getElementById("quiz-root");
const progressBar = document.getElementById("progress-bar");
const resultsEl = document.getElementById("results");

function renderQuestion(index) {
  const item = QUESTIONS[index];
  const card = document.createElement("div");
  card.className = "module quiz-card active";
  card.innerHTML = `
    <span class="qtag">${item.tag} · Pergunta ${index + 1} de ${QUESTIONS.length}</span>
    <h3>${item.q}</h3>
    <div class="options">
      ${item.options.map((opt, i) => `<button class="option" data-i="${i}">${opt}</button>`).join("")}
    </div>
    <div class="feedback" id="feedback-${index}"></div>
    <div class="quiz-nav">
      <button class="btn ghost" id="prev-btn" type="button" ${index === 0 ? "disabled style='opacity:.4;cursor:default;'" : ""}>← Anterior</button>
      <button class="btn primary" id="next-btn" type="button" disabled style="opacity:.4;cursor:default;">${index === QUESTIONS.length - 1 ? "Ver resultado" : "Próxima →"}</button>
    </div>
  `;
  root.innerHTML = "";
  root.appendChild(card);

  const optionButtons = card.querySelectorAll(".option");
  const feedbackEl = card.querySelector(`#feedback-${index}`);
  const nextBtn = card.querySelector("#next-btn");
  const prevBtn = card.querySelector("#prev-btn");

  if (answers[index] !== null) {
    lockAnswer(optionButtons, feedbackEl, item, answers[index]);
    nextBtn.disabled = false;
    nextBtn.style.opacity = 1;
    nextBtn.style.cursor = "pointer";
  }

  optionButtons.forEach((btn) => {
    btn.addEventListener("click", () => {
      if (answers[index] !== null) return;
      const chosen = parseInt(btn.dataset.i, 10);
      answers[index] = chosen;
      lockAnswer(optionButtons, feedbackEl, item, chosen);
      nextBtn.disabled = false;
      nextBtn.style.opacity = 1;
      nextBtn.style.cursor = "pointer";
      updateProgress();
    });
  });

  nextBtn.addEventListener("click", () => {
    if (index === QUESTIONS.length - 1) {
      showResults();
    } else {
      current = index + 1;
      renderQuestion(current);
    }
  });

  if (prevBtn) {
    prevBtn.addEventListener("click", () => {
      current = index - 1;
      renderQuestion(current);
    });
  }

  updateProgress();
}

function lockAnswer(optionButtons, feedbackEl, item, chosen) {
  optionButtons.forEach((b) => (b.disabled = true));
  const correctBtn = optionButtons[item.correct];
  const chosenBtn = optionButtons[chosen];
  correctBtn.classList.add("correct");
  const isRight = chosen === item.correct;
  if (!isRight) chosenBtn.classList.add("incorrect");

  feedbackEl.classList.add("show", isRight ? "ok" : "no");
  feedbackEl.innerHTML = `
    <div class="verdict ${isRight ? "ok-text" : "no-text"}">${isRight ? "✅ Certo!" : "❌ Não é essa — vamos entender por quê."}</div>
    <div>${item.explain}</div>
    <div class="example"><b>Exemplo para fixar:</b> ${item.example}</div>
  `;
}

function updateProgress() {
  const answered = answers.filter((a) => a !== null).length;
  const pct = Math.round((answered / QUESTIONS.length) * 100);
  progressBar.style.width = pct + "%";
}

function showResults() {
  root.innerHTML = "";
  const score = answers.reduce((acc, a, i) => acc + (a === QUESTIONS[i].correct ? 1 : 0), 0);
  const pct = Math.round((score / QUESTIONS.length) * 100);

  resultsEl.classList.add("show");
  document.getElementById("score-ring").style.setProperty("--pct", pct);
  document.getElementById("score-text").textContent = `${score}/${QUESTIONS.length}`;

  let msg;
  if (score === QUESTIONS.length) msg = "Perfeito! Você dominou indução eletromagnética. Releia só o atalho mental de vez em quando para manter fresco.";
  else if (score >= 7) msg = "Muito bom! Reveja no guia os módulos das perguntas erradas abaixo — são pontos pequenos de ajustar.";
  else if (score >= 4) msg = "Bom começo. Volte ao guia de estudo e releia com calma os módulos indicados abaixo antes de repetir o quiz.";
  else msg = "Sem problema — é bastante conteúdo novo. Releia o guia do início, focando nas imagens mentais e nos exemplos, e tente de novo.";
  document.getElementById("score-msg").textContent = msg;

  const reviewList = document.getElementById("review-list");
  reviewList.innerHTML = QUESTIONS.map((item, i) => {
    const isRight = answers[i] === item.correct;
    return `
      <div class="review-item ${isRight ? "right" : "wrong"}">
        <div style="font-weight:700; margin-bottom:4px;">${isRight ? "✅" : "❌"} ${item.tag}</div>
        <div style="margin-bottom:6px;">${item.q}</div>
        ${isRight ? "" : `<div style="color:var(--muted); font-size:0.92rem;"><b>Sua resposta:</b> ${item.options[answers[i]]}<br><b>Correta:</b> ${item.options[item.correct]}<br>${item.explain}</div>`}
      </div>
    `;
  }).join("");

  progressBar.style.width = "100%";
}

document.getElementById("retry-btn").addEventListener("click", () => {
  current = 0;
  answers = new Array(QUESTIONS.length).fill(null);
  resultsEl.classList.remove("show");
  renderQuestion(0);
  window.scrollTo({ top: 0, behavior: "smooth" });
});

renderQuestion(0);
