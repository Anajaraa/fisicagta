# -*- coding: utf-8 -*-
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

ACCENT = RGBColor(0x13, 0x72, 0xC9)
GOOD = RGBColor(0x0E, 0x9F, 0x5F)
MUTED = RGBColor(0x52, 0x5F, 0x7A)
DARK = RGBColor(0x1A, 0x21, 0x30)

doc = Document()

# Base style
style = doc.styles["Normal"]
style.font.name = "Calibri"
style.font.size = Pt(11)
style.font.color.rgb = DARK

def set_cell_shading(cell, color_hex):
    shd = OxmlElement("w:shd")
    shd.set(qn("w:fill"), color_hex)
    cell._tc.get_or_add_tcPr().append(shd)

def add_box(doc_, title, body_lines, color=ACCENT):
    p = doc_.add_paragraph()
    p.paragraph_format.space_before = Pt(6)
    run = p.add_run(title)
    run.bold = True
    run.font.color.rgb = color
    for line in body_lines:
        bp = doc_.add_paragraph(line)
        bp.paragraph_format.left_indent = Inches(0.15)
    doc_.add_paragraph()

def add_recall(doc_, text):
    p = doc_.add_paragraph()
    run = p.add_run("FIXOU: ")
    run.bold = True
    run.font.color.rgb = GOOD
    p.add_run(text)
    p.paragraph_format.space_after = Pt(16)

# ---------- COVER ----------
title = doc.add_heading("Indução Eletromagnética em 2 Horas", level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub = doc.add_paragraph("Guia de estudo com imagens mentais, exemplos concretos, comparações simples e um atalho mental")
sub.alignment = WD_ALIGN_PARAGRAPH.CENTER
sub.runs[0].italic = True
sub.runs[0].font.color.rgb = MUTED
doc.add_paragraph()
info = doc.add_paragraph("7 módulos · ~15 min cada · 1 atalho mental · quiz online linkado ao final")
info.alignment = WD_ALIGN_PARAGRAPH.CENTER
info.runs[0].font.color.rgb = MUTED
doc.add_page_break()

# ---------- TOC ----------
doc.add_heading("Roteiro dos 120 minutos", level=1)
toc_items = [
    "1. Força magnética (Lei de Lorentz)",
    "2. Fluxo magnético (Φ)",
    "3. Lei de Faraday (f.e.m. induzida)",
    "4. Lei de Lenz (o sentido da corrente)",
    "5. Lendo gráficos de Φ × t",
    "6. Corrente alternada vs. contínua",
    "7. Aplicações do mundo real",
    "8. Atalho mental: o Ímã Preguiçoso e a Bobina Birrenta",
    "9. Link do quiz online",
]
for it in toc_items:
    doc.add_paragraph(it, style="List Number")
doc.add_page_break()

# ---------- MODULE helper ----------
def module(num, title_, tag, intro_paras, formula, image_text, example_paras, compare_text, recall_text, compare_table=None):
    h = doc.add_heading(f"{num}. {title_}", level=1)
    tagp = doc.add_paragraph(tag)
    tagp.runs[0].italic = True
    tagp.runs[0].font.color.rgb = MUTED

    for para in intro_paras:
        doc.add_paragraph(para)

    if formula:
        fp = doc.add_paragraph()
        fr = fp.add_run(formula)
        fr.bold = True
        fr.font.size = Pt(13)
        fr.font.color.rgb = ACCENT

    add_box(doc, "🧠 Imagem mental", [image_text], ACCENT)
    add_box(doc, "🧮 Exemplo concreto", example_paras, GOOD)

    if compare_table:
        cp = doc.add_paragraph()
        cr = cp.add_run("🔁 Comparação simples")
        cr.bold = True
        cr.font.color.rgb = RGBColor(0xC9, 0x7D, 0x10)
        table = doc.add_table(rows=1, cols=len(compare_table[0]))
        table.style = "Light Grid Accent 1"
        hdr = table.rows[0].cells
        for i, h_ in enumerate(compare_table[0]):
            hdr[i].text = h_
        for row in compare_table[1:]:
            cells = table.add_row().cells
            for i, val in enumerate(row):
                cells[i].text = val
        doc.add_paragraph()
    else:
        add_box(doc, "🔁 Comparação simples", [compare_text], RGBColor(0xC9, 0x7D, 0x10))

    add_recall(doc, recall_text)
    doc.add_paragraph()

# Module 1
module(
    1, "Força magnética sobre uma carga (Força de Lorentz)",
    "Antes de falar em \"induzir corrente\", veja como um campo magnético empurra uma carga que já está se movendo.",
    [
        "Quando uma carga elétrica q se move com velocidade v dentro de um campo magnético B, ela sofre uma força. "
        "Essa força só existe se a carga estiver em movimento e não for paralela ao campo:"
    ],
    "F = q · v · B · sen(θ)",
    "Pense num rio (o campo magnético, sempre fluindo na mesma direção) e um nadador (a carga) atravessando-o. "
    "Se o nadador nadar exatamente no sentido da correnteza, ele não sente nenhum empurrão de lado. Se nadar "
    "perpendicular à correnteza, sente o empurrão máximo, que o desvia para o lado. Essa \"correnteza que empurra "
    "de lado\" é a força magnética — e ela some quando v e B são paralelos (sen 0° = 0).",
    [
        "Uma partícula com carga Q = 3,2×10⁻¹⁹ C entra numa região com campo magnético de 3 T, com velocidade de "
        "2,0×10⁶ m/s, formando um ângulo θ com o campo tal que sen θ = 1/3.",
        "F = q·v·B·senθ = 3,2×10⁻¹⁹ × 2,0×10⁶ × 3 × (1/3) ≈ 6,4×10⁻¹³ N",
        "Pouquíssimo em números absolutos — mas é essa força minúscula que curva o caminho de elétrons dentro de um "
        "tubo de TV antigo, num acelerador de partículas, ou na aurora boreal.",
    ],
    "É como empurrar uma bicicleta: se você empurrar na mesma direção que ela já está andando (para frente), ela "
    "não vira. Se empurrar de lado, ela vira. O campo magnético só \"vira\" cargas que cruzam suas linhas de força "
    "— nunca as que andam exatamente junto com elas.",
    "sem movimento relativo entre carga e campo, ou com movimento paralelo ao campo, não existe força magnética.",
)

# Module 2
module(
    2, "Fluxo magnético (Φ)",
    "A grandeza que a Lei de Faraday vai observar \"variar\" — entenda o que ela mede antes de tudo.",
    [
        "O fluxo magnético mede quantas linhas de campo magnético atravessam uma superfície (por exemplo, a área "
        "de uma espira):"
    ],
    "Φ = B · A · cos(θ)",
    "Imagine um varal (a espira) estendido no quintal num dia de sol. O \"fluxo\" é a quantidade de luz solar que "
    "passa através da área do varal. Se o sol está bem acima (perpendicular ao varal), passa o máximo de luz. Se o "
    "varal está de perfil para o sol (paralelo aos raios), quase nenhuma luz atravessa — fluxo quase zero, mesmo "
    "que o sol continue brilhando com a mesma intensidade.",
    [
        "Uma espira circular de raio 30,0 cm (A = π·r² ≈ 0,27 m²) está perpendicular a um campo magnético. Se "
        "B = 0,010 T, o fluxo através dela é:",
        "Φ = B · A = 0,010 × 0,27 ≈ 2,7×10⁻³ Wb (weber, a unidade de fluxo magnético)",
    ],
    "Fluxo magnético está para o campo magnético assim como \"quantidade de chuva que molhou o guarda-chuva\" está "
    "para \"intensidade da chuva\". Pode estar chovendo forte (B grande), mas se você inclinar o guarda-chuva de "
    "lado (cos θ pequeno) ou ele for pequeno (A pequena), pouca água (fluxo) realmente passa por ele.",
    "Φ depende de três coisas — a intensidade do campo, a área da espira e o ângulo entre eles. Mexer em qualquer "
    "uma delas muda o fluxo.",
)

# Module 3
module(
    3, "Lei de Faraday: a f.e.m. induzida",
    "O coração de toda a matéria: corrente elétrica só nasce quando o fluxo muda.",
    [
        "A Lei de Faraday diz que surge uma força eletromotriz (f.e.m., medida em volts) sempre que o fluxo "
        "magnético através de um circuito varia com o tempo. Quanto mais espiras (N) e quanto mais rápida a "
        "variação, maior a f.e.m.:"
    ],
    "ε = N · (ΔΦ / Δt)",
    "Pense numa esponja cheia de água parada na sua mão: nada escorre, não importa o quão encharcada ela esteja "
    "(fluxo constante = zero corrente). Agora aperte a esponja: só quando você muda a pressão (varia o fluxo) a "
    "água (corrente) sai. Parou de apertar? A água para de sair de novo, mesmo que a esponja ainda esteja "
    "encharcada. É a mudança que gera corrente, nunca o estado parado.",
    [
        "(Exemplo real de prova, equipamento de ressonância magnética) Um solenoide com N = 10 espiras, raio "
        "30,0 cm (A ≈ 0,27 m²), está num campo magnético uniforme perpendicular ao plano das espiras. Em 0,001 s, "
        "o campo varia de 0 a 0,010 T.",
        "ΔΦ/Δt = A · (ΔB/Δt) = 0,27 × (0,010 / 0,001) = 0,27 × 10 = 2,7 Wb/s",
        "ε = N · ΔΦ/Δt = 10 × 2,7 = 27,0 V",
        "Esse é exatamente o princípio por trás de equipamentos de ressonância magnética: campo variando "
        "rapidamente dentro de bobinas gera as correntes que formam a imagem.",
    ],
    None,
    "\"parado não gera, só mudança cria\" — grave essa frase, ela resume a Lei de Faraday inteira.",
    compare_table=[
        ["Situação", "Fluxo", "Gera corrente?"],
        ["Ímã parado dentro da espira", "constante", "Não"],
        ["Ímã se aproximando ou se afastando", "variando", "Sim"],
        ["Espira girando num campo fixo", "variando (ângulo muda)", "Sim"],
        ["Corrente contínua constante na bobina vizinha", "constante", "Não (só ao ligar/desligar)"],
    ],
)

# Module 4
module(
    4, "Lei de Lenz: o sentido da corrente induzida",
    "Faraday diz \"quanto\". Lenz diz \"para onde\".",
    [
        "A corrente induzida sempre circula num sentido que se opõe à variação do fluxo que a criou. Isso é, na "
        "prática, uma consequência da conservação de energia: a natureza não te dá energia de graça."
    ],
    None,
    "Imagine empurrar uma porta de vaivém. Toda vez que você empurra para entrar, ela gera uma resistência contra "
    "sua mão que tenta te empurrar de volta. A corrente induzida é exatamente essa \"resistência teimosa\": se "
    "você aproxima um ímã da espira, a corrente induzida cria seu próprio campo magnético para repelir o ímã "
    "(dificultar a aproximação). Se você afasta o ímã, a corrente inverte e passa a atrair o ímã de volta "
    "(dificultar o afastamento). A espira sempre \"briga\" contra quem mexeu nela.",
    [
        "Um ímã em barra é aproximado e depois afastado de uma espira ligada a um amperímetro, ao longo de um "
        "eixo que passa pelo centro da espira. Resultado: surge corrente induzida tanto na aproximação quanto no "
        "afastamento — só que em sentidos opostos. Se o ímã ficar parado em qualquer ponto do eixo, a corrente é "
        "zero, não importa a distância.",
    ],
    "É como um amigo chato que sempre faz o oposto do que você quer: se você tenta empurrá-lo para frente, ele "
    "força para trás; se você puxa para trás, ele força para frente. A corrente induzida é fisicamente \"chata\" "
    "com qualquer mudança — e é exatamente por isso que freios magnéticos de montanha-russa funcionam (a corrente "
    "induzida nos trilhos metálicos freia o carrinho, se opondo ao seu movimento).",
    "a corrente induzida nunca ajuda a mudança que a criou — ela sempre se opõe. É oposição, não cooperação.",
)

# Module 5
module(
    5, "Lendo gráficos de Φ × t",
    "Esse é o tipo de questão que mais derruba gente que \"sabe a fórmula\" mas não sabe ler o desenho.",
    [
        "Como ε = N·ΔΦ/Δt, e ΔΦ/Δt é exatamente a inclinação (declividade) da reta no gráfico Φ × t, basta olhar "
        "o desenho:"
    ],
    None,
    "Pense no gráfico como o perfil de uma trilha de montanha vista de lado. Trecho subindo ou descendo = ladeira "
    "íngreme = você \"sente\" a inclinação (há f.e.m.). Trecho reto e plano = não há ladeira nenhuma = f.e.m. "
    "zero, mesmo que você esteja bem alto (fluxo grande, mas constante).",
    [
        "Uma bobina de N = 200 espiras tem o fluxo por espira subindo de 0 a 0,002 Wb entre t = 0 e t = 0,2 s, "
        "depois ficando constante em 0,002 Wb até t = 0,6 s, e finalmente descendo a zero entre t = 0,6 s e "
        "t = 0,8 s.",
        "Durante a subida (0 a 0,2 s): ΔΦ/Δt = 0,002/0,2 = 0,01 Wb/s → ε = 200 × 0,01 = 2,0 V",
        "No trecho plano (0,2 a 0,6 s): ΔΦ/Δt = 0 → ε = 0 V (mesmo com fluxo máximo!)",
        "Na descida (0,6 a 0,8 s): mesma inclinação em módulo → ε = 2,0 V novamente (sentido invertido)",
    ],
    "É como velocímetro vs. odômetro num carro parado num sinal vermelho: o odômetro (fluxo acumulado) pode marcar "
    "um número altíssimo, mas o velocímetro (a taxa de variação, equivalente à f.e.m.) marca zero porque o carro "
    "não está andando naquele instante.",
    "trecho inclinado no gráfico = gera tensão; trecho plano (mesmo que alto) = tensão zero.",
)

# Module 6
module(
    6, "Corrente alternada vs. corrente contínua",
    "Por que quase toda indução \"útil\" usa corrente alternada.",
    [],
    None,
    "Corrente contínua é uma pessoa andando sempre na mesma direção, em linha reta e em velocidade constante — "
    "depois do arranque inicial, nada muda, então não \"balança\" o fluxo. Corrente alternada é alguém numa "
    "cadeira de balanço: vai e volta, vai e volta, sem parar — e é esse vaivém constante que mantém o fluxo "
    "sempre variando, gerando indução contínua no tempo.",
    [
        "Um carregador de celular sem fio tem uma bobina na base. Se essa bobina fosse alimentada por corrente "
        "contínua constante, geraria um pulso de indução só no instante de ligar e desligar — e nada entre esses "
        "dois momentos. Por isso a base usa corrente alternada: o fluxo está sempre subindo e descendo, então a "
        "bobina do celular recebe energia continuamente, enquanto estiver próxima.",
    ],
    "A lâmpada da sua casa pisca 100 ou 120 vezes por segundo (acompanhando a corrente alternada de 50 ou 60 Hz), "
    "mas seu olho não percebe porque é rápido demais — exatamente como um ventilador girando rápido parece um "
    "disco sólido. A luz \"parece\" constante, mas eletricamente está sempre variando.",
    "indução contínua e sustentada no tempo exige corrente alternada na fonte — corrente contínua constante não "
    "sustenta f.e.m. induzida.",
)

# Module 7 - applications (custom, not using the generic helper due to multiple short examples)
doc.add_heading("7. Aplicações do mundo real", level=1)
tagp = doc.add_paragraph("Toda a teoria acima em quatro aparelhos que você já usou.")
tagp.runs[0].italic = True
tagp.runs[0].font.color.rgb = MUTED

apps = [
    ("🔌 Ignição automotiva (transformador)",
     "A bateria do carro (12 V, baixa tensão) alimenta o enrolamento primário de uma bobina de ignição. Ao cortar "
     "essa corrente rapidamente, o fluxo cai bruscamente, induzindo uma tensão enorme no enrolamento secundário — "
     "alta o bastante para criar a centelha nas velas. É a Lei de Faraday pura: ΔΦ/Δt gigante por causa do corte "
     "abrupto de corrente."),
    ("🍳 Fogão de indução",
     "Uma bobina embaixo do vidro gera um campo magnético alternado. A base da panela (metálica) funciona como "
     "uma \"espira de uma volta\": o fluxo variando dentro dela induz correntes que, por efeito Joule (resistência "
     "do metal), aquecem a panela diretamente — o vidro em si não esquenta, só a panela."),
    ("📶 Carregador sem fio",
     "A base gera um campo magnético alternado; a bobina dentro do celular \"sente\" esse fluxo variando e gera "
     "uma f.e.m. induzida, convertida em corrente para carregar a bateria. Sem contato elétrico direto — só o "
     "fluxo variável atravessando o espaço entre as duas bobinas."),
    ("💧 Usina hidrelétrica (geração de energia)",
     "A água em movimento gira turbinas conectadas a bobinas que giram dentro de campos magnéticos fixos (ou "
     "vice-versa). Ao girar, o ângulo θ do fluxo (Φ = B·A·cosθ) muda constantemente, criando uma f.e.m. alternada "
     "— essa é a origem de praticamente toda a energia elétrica que chega à sua casa."),
]
for h, body in apps:
    add_box(doc, h, [body], GOOD)
add_recall(doc, "todos esses aparelhos fazem a mesma coisa — criam um fluxo magnético que varia de propósito, "
                "para colher a f.e.m. induzida que essa variação gera.")
doc.add_paragraph()
doc.add_page_break()

# ---------- MNEMONIC ----------
doc.add_heading("8. Atalho mental: \"O Ímã Preguiçoso e a Bobina Birrenta\"", level=1)
doc.add_paragraph("Para lembrar de tudo acima em 10 segundos, imagine esta historinha sempre que ler uma questão "
                   "de indução:")

story = [
    ("🧲😴 O ímã preguiçoso:", "parado dentro ou perto de uma espira, ele não faz nada. Nenhuma corrente nasce de "
     "um ímã parado — \"parado não gera\"."),
    ("🏃💨 Alguém sacode o ímã", "(ele se aproxima, se afasta, ou gira): isso muda o fluxo que atravessa a espira. "
     "Só mudança cria f.e.m. — e quanto mais rápido o sacode e quanto mais espiras (N) a bobina tiver, mais forte "
     "é a tensão gerada (ε = N·ΔΦ/Δt)."),
    ("😤🔁 A bobina birrenta:", "ela não gosta de ser incomodada, então a corrente que nasce nela sempre tenta "
     "atrapalhar quem a sacudiu — empurra o ímã para longe se ele se aproxima, puxa de volta se ele se afasta "
     "(Lei de Lenz)."),
    ("📈〰️ Se alguém ficar sacudindo o ímã pra lá e pra cá sem parar", "(corrente alternada), a bobina gera "
     "tensão o tempo todo — é assim que carregador sem fio, fogão de indução e usina hidrelétrica funcionam."),
]
for lead, rest in story:
    p = doc.add_paragraph()
    r1 = p.add_run(lead + " ")
    r1.bold = True
    r1.font.color.rgb = ACCENT
    p.add_run(rest)

doc.add_paragraph()
add_recall(doc, "\"Parado não gera, só mudança cria — e a bobina sempre se vira contra quem mexeu nela.\"")

doc.add_page_break()

# ---------- QUIZ LINK ----------
doc.add_heading("9. Quiz online", level=1)
doc.add_paragraph(
    "O quiz inteligente com 10 perguntas, correção automática, explicação dos erros e exemplos extras está "
    "disponível online (link inserido após o deploy no Vercel — veja a página index.html / quiz.html publicada)."
)
p = doc.add_paragraph()
r = p.add_run("Dica: ")
r.bold = True
p.add_run("faça o quiz logo após terminar de ler este guia, enquanto o conteúdo ainda está fresco. Erros no quiz "
          "indicam exatamente qual módulo deste documento você deve reler.")

doc.save("Eletromagnetismo_Guia_de_Estudo.docx")
print("OK: Eletromagnetismo_Guia_de_Estudo.docx gerado")
