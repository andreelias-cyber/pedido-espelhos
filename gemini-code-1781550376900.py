# Definindo o conteúdo do arquivo index.html melhorado
html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>André Elias Representações - Pedido de Espelhos</title>
<style>
  @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Barlow+Condensed:wght@600;700&display=swap');

  :root {
    --azul: #2B4C7E;
    --azul-escuro: #1A3052;
    --azul-claro: #F0F4F8;
    --azul-destaque: #3A6EA5;
    --laranja: #F58220;
    --laranja-hover: #D96B14;
    --cinza-bg: #F8FAFC;
    --cinza-borda: #E2E8F0;
    --cinza-texto: #64748B;
    --texto-principal: #1E293B;
    --branco: #ffffff;
    --sombra-sm: 0 1px 3px rgba(0,0,0,0.05);
    --sombra-md: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -1px rgba(0,0,0,0.03);
    --sombra-lg: 0 10px 15px -3px rgba(0,0,0,0.08), 0 4px 6px -2px rgba(0,0,0,0.04);
    --radius: 12px;
  }

  * { box-sizing: border-box; margin: 0; padding: 0; }

  body {
    font-family: 'Inter', sans-serif;
    background: var(--cinza-bg);
    color: var(--texto-principal);
    min-height: 100vh;
    -webkit-font-smoothing: antialiased;
  }

  /* HEADER */
  header {
    background: var(--branco);
    padding: 0 32px;
    height: 80px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
    box-shadow: var(--sombra-sm);
    border-bottom: 1px solid var(--cinza-borda);
  }
  
  .logo-container {
    display: flex;
    align-items: center;
    height: 100%;
  }

  .logo img {
    height: 56px;
    width: auto;
    display: block;
    object-fit: contain;
  }

  .carrinho-btn {
    position: relative;
    background: var(--azul);
    border: none;
    border-radius: 8px;
    color: var(--branco);
    padding: 12px 24px;
    cursor: pointer;
    font-size: 0.95rem;
    font-weight: 600;
    display: flex;
    align-items: center;
    gap: 10px;
    transition: all 0.2s ease;
    box-shadow: var(--sombra-sm);
  }
  
  .carrinho-btn:hover { 
    background: var(--azul-escuro); 
    transform: translateY(-1px);
    box-shadow: var(--sombra-md);
  }
  
  .badge {
    background: var(--laranja);
    color: var(--branco);
    border-radius: 50%;
    width: 22px; 
    height: 22px;
    display: flex; 
    align-items: center; 
    justify-content: center;
    font-size: 0.75rem;
    font-weight: 700;
    position: absolute;
    top: -8px; 
    right: -8px;
    border: 2px solid var(--branco);
    box-shadow: var(--sombra-sm);
  }

  /* BANNER PRINCIPAL */
  .banner-loja {
    background: linear-gradient(135deg, #1A3052 0%, #2B4C7E 100%);
    padding: 40px 32px;
    display: flex;
    align-items: center;
    gap: 32px;
    justify-content: center;
    border-bottom: 4px solid var(--laranja);
  }
  
  .banner-logo {
    height: 90px;
    width: auto;
    flex-shrink: 0;
    background: var(--branco);
    border-radius: 8px;
    padding: 10px 16px;
    box-shadow: var(--sombra-md);
  }
  
  .banner-texto {
    color: var(--branco);
  }
  
  .banner-titulo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 2rem;
    font-weight: 700;
    text-transform: uppercase;
    letter-spacing: 0.5px;
    color: var(--branco);
    margin-bottom: 6px;
  }
  
  .banner-sub {
    font-size: 1rem;
    color: #E2E8F0;
    max-width: 600px;
    line-height: 1.5;
  }

  /* BUSCA */
  .busca-wrap {
    max-width: 600px;
    margin: 32px auto 0;
    padding: 0 16px;
  }
  
  .busca-rel { position: relative; }
  
  .busca-wrap input {
    width: 100%;
    padding: 14px 18px 14px 48px;
    border: 1px solid var(--cinza-borda);
    border-radius: var(--radius);
    font-size: 1rem;
    font-family: 'Inter', sans-serif;
    background: var(--branco);
    outline: none;
    transition: all 0.2s ease;
    color: var(--texto-principal);
    box-shadow: var(--sombra-sm);
  }
  
  .busca-wrap input:focus { 
    border-color: var(--azul-destaque); 
    box-shadow: 0 0 0 4px rgba(58, 110, 165, 0.15); 
  }
  
  .busca-icon {
    position: absolute;
    left: 18px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 1.1rem;
    color: var(--cinza-texto);
    pointer-events: none;
  }

  /* MAIN CONTENT */
  .main {
    max-width: 1200px;
    margin: 0 auto;
    padding: 40px 24px 120px;
  }

  .secao-titulo {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    color: var(--azul-escuro);
    margin-bottom: 24px;
    padding-bottom: 12px;
    border-bottom: 2px solid var(--cinza-borda);
    display: flex;
    align-items: center;
    gap: 10px;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  
  .secao-titulo::before {
    content: '';
    display: inline-block;
    width: 6px; 
    height: 24px;
    background: var(--laranja);
    border-radius: 4px;
  }

  /* GRID DE PRODUTOS */
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
    gap: 24px;
  }

  .card {
    background: var(--branco);
    border-radius: var(--radius);
    box-shadow: var(--sombra-md);
    overflow: hidden;
    display: flex;
    flex-direction: column;
    transition: all 0.2s ease;
    border: 1px solid var(--cinza-borda);
  }
  
  .card:hover { 
    transform: translateY(-4px); 
    box-shadow: var(--sombra-lg);
    border-color: var(--azul-destaque);
  }
  
  .card.no-carrinho { 
    border: 2px solid var(--laranja); 
  }

  .card-img-wrap {
    width: 100%;
    aspect-ratio: 1 / 1;
    overflow: hidden;
    background: #F1F5F9;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
    border-bottom: 1px solid var(--cinza-borda);
  }
  
  .card-img {
    width: 100%;
    height: 100%;
    object-fit: cover;
    display: block;
    transition: transform 0.3s ease;
  }
  
  .card:hover .card-img { transform: scale(1.05); }

  .card-body {
    padding: 16px;
    flex: 1;
    display: flex;
    flex-direction: column;
    gap: 6px;
  }
  
  .card-cod {
    font-size: 0.75rem;
    color: var(--cinza-texto);
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 0.5px;
  }
  
  .card-nome {
    font-family: 'Inter', sans-serif;
    font-size: 1.1rem;
    font-weight: 600;
    color: var(--azul-escuro);
    line-height: 1.4;
  }
  
  .card-desc {
    font-size: 0.85rem;
    color: var(--cinza-texto);
    line-height: 1.4;
  }
  
  .card-preco {
    font-size: 1.25rem;
    font-weight: 700;
    color: var(--azul);
    margin-top: auto;
    padding-top: 8px;
  }
  
  .card-preco-unit {
    font-size: 0.8rem;
    font-weight: 400;
    color: var(--cinza-texto);
    margin-left: 2px;
  }

  /* Info de múltiplo */
  .info-multiplo {
    font-size: 0.8rem;
    color: var(--laranja);
    background: #FFF7ED;
    border: 1px solid #FFEDD5;
    padding: 6px 10px;
    border-radius: 6px;
    font-weight: 600;
    display: inline-flex;
    align-items: center;
    gap: 6px;
    margin-top: 4px;
  }

  /* CONTROLE DE QTD NO CARD */
  .card-footer {
    padding: 0 16px 16px 16px;
    display: flex;
    flex-direction: column;
    gap: 10px;
  }

  .footer-row {
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .qty-ctrl {
    display: flex;
    align-items: center;
    border: 1px solid var(--cinza-borda);
    border-radius: 8px;
    overflow: hidden;
    flex: 1;
    background: var(--azul-claro);
    height: 38px;
  }
  
  .qty-ctrl button {
    background: none;
    border: none;
    width: 36px; 
    height: 100%;
    font-size: 1.2rem;
    cursor: pointer;
    color: var(--azul);
    font-weight: 600;
    transition: background 0.15s;
  }
  
  .qty-ctrl button:hover { background: #E2E8F0; }
  
  .qty-val {
    flex: 1;
    text-align: center;
    font-weight: 700;
    font-size: 1rem;
    color: var(--texto-principal);
  }
  
  .btn-add {
    background: var(--azul);
    color: var(--branco);
    border: none;
    border-radius: 8px;
    padding: 0 16px;
    height: 38px;
    font-size: 0.85rem;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s ease;
    white-space: nowrap;
    font-family: 'Inter', sans-serif;
  }
  
  .btn-add:hover { background: var(--azul-escuro); }
  .btn-add.adicionado { background: #10B981; }

  /* PANEL CARRINHO LATERAL */
  .overlay {
    display: none;
    position: fixed;
    inset: 0;
    background: rgba(15, 23, 42, 0.6);
    backdrop-filter: blur(4px);
    z-index: 199;
  }
  .overlay.ativo { display: block; }

  .carrinho-panel {
    position: fixed;
    top: 0; right: -460px;
    width: 440px;
    max-width: 100vw;
    height: 100vh;
    background: var(--branco);
    z-index: 200;
    transition: right 0.3s cubic-bezier(.4,0,.2,1);
    display: flex;
    flex-direction: column;
    box-shadow: var(--sombra-lg);
  }
  .carrinho-panel.aberto { right: 0; }

  .carrinho-header {
    background: var(--azul-escuro);
    color: var(--branco);
    padding: 24px;
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
  .carrinho-header h2 {
    font-family: 'Barlow Condensed', sans-serif;
    font-size: 1.5rem;
    font-weight: 700;
    letter-spacing: 0.5px;
    text-transform: uppercase;
  }
  
  .fechar-btn {
    background: rgba(255,255,255,0.1);
    border: none;
    color: var(--branco);
    width: 36px; height: 36px;
    border-radius: 8px;
    font-size: 1.2rem;
    cursor: pointer;
    display: flex; align-items: center; justify-content: center;
    transition: background 0.15s;
  }
  .fechar-btn:hover { background: rgba(255,255,255,0.2); }

  .carrinho-itens {
    flex: 1;
    overflow-y: auto;
    padding: 20px;
    display: flex;
    flex-direction: column;
    gap: 12px;
  }

  .carrinho-vazio {
    text-align: center;
    color: var(--cinza-texto);
    padding: 80px 20px;
  }
  .carrinho-vazio .icone { font-size: 3.5rem; margin-bottom: 16px; opacity: 0.7; }
  .carrinho-vazio p { font-size: 1rem; line-height: 1.6; }

  .item-cart {
    background: var(--cinza-bg);
    border-radius: 8px;
    padding: 12px;
    display: flex;
    gap: 12px;
    align-items: center;
    border: 1px solid var(--cinza-borda);
  }
  
  .item-cart-img {
    width: 56px; 
    height: 56px;
    border-radius: 6px;
    object-fit: cover;
    background: #E2E8F0;
    flex-shrink: 0;
  }
  
  .item-info { flex: 1; min-width: 0; }
  .item-info .cod { font-size: 0.7rem; color: var(--cinza-texto); font-weight: 600; text-transform: uppercase; }
  .item-info .nome { font-size: 0.95rem; font-weight: 600; color: var(--azul-escuro); white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
  .item-info .subtotal { font-size: 0.95rem; color: #10B981; font-weight: 700; margin-top: 2px; }
  .item-info .multiplo-info { font-size: 0.75rem; color: var(--laranja); font-weight: 500; }

  .item-cart-ctrl {
    display: flex;
    align-items: center;
    gap: 8px;
    border: 1px solid var(--cinza-borda);
    background: var(--branco);
    padding: 4px;
    border-radius: 6px;
  }
  
  .mini-btn {
    background: none;
    border: none;
    border-radius: 4px;
    width: 26px; height: 26px;
    font-size: 1rem;
    cursor: pointer;
    font-weight: 600;
    color: var(--azul);
    display: flex; align-items: center; justify-content: center;
    transition: all 0.15s;
  }
  
  .mini-btn:hover { background: var(--azul-claro); }
  .mini-btn.remover { color: #EF4444; }
  .mini-btn.remover:hover { background: #FEE2E2; }
  .item-qty-val { font-weight: 700; font-size: 0.9rem; min-width: 24px; text-align: center; }

  .carrinho-footer {
    padding: 24px;
    border-top: 1px solid var(--cinza-borda);
    display: flex;
    flex-direction: column;
    gap: 16px;
    background: #F8FAFC;
  }
  
  .total-linha {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 4px;
  }
  
  .total-label { font-size: 1rem; font-weight: 500; color: var(--cinza-texto); }
  .total-valor { font-size: 1.65rem; font-weight: 700; color: var(--azul-escuro); }

  .campo-nome {
    width: 100%;
    padding: 14px;
    border: 1px solid var(--cinza-borda);
    border-radius: 8px;
    font-size: 0.95rem;
    font-family: 'Inter', sans-serif;
    outline: none;
    transition: all 0.2s ease;
    background: var(--branco);
    color: var(--texto-principal);
    box-shadow: var(--sombra-sm);
  }
  
  .campo-nome:focus { 
    border-color: var(--azul-destaque); 
    box-shadow: 0 0 0 4px rgba(58, 110, 165, 0.15); 
  }

  .btn-zap {
    background: #25D366;
    color: var(--branco);
    border: none;
    border-radius: 8px;
    padding: 14px;
    font-size: 1rem;
    font-weight: 600;
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 10px;
    transition: all 0.2s ease;
    font-family: 'Inter', sans-serif;
    box-shadow: var(--sombra-sm);
  }
  
  .btn-zap:hover { background: #1EA952; transform: translateY(-1px); box-shadow: var(--sombra-md); }

  .nenhum {
    text-align: center;
    color: var(--cinza-texto);
    padding: 60px 20px;
    font-size: 1rem;
    grid-column: 1 / -1;
  }

  /* RESPONSIVIDADE */
  @media (max-width: 768px) {
    header { padding: 0 16px; height: 70px; }
    .logo img { height: 44px; }
    .carrinho-btn { padding: 10px 16px; font-size: 0.9rem; }
    .banner-loja { flex-direction: column; text-align: center; gap: 16px; padding: 32px 16px; }
    .banner-texto { display: flex; flex-direction: column; align-items: center; }
    .banner-titulo { font-size: 1.6rem; }
    .banner-sub { font-size: 0.9rem; }
    .banner-logo { height: 70px; }
    .grid { grid-template-columns: repeat(auto-fill, minmax(180px, 1fr)); gap: 16px; }
    .card-body { padding: 12px; gap: 4px; }
    .card-nome { font-size: 0.95rem; }
    .card-preco { font-size: 1.1rem; }
    .carrinho-panel { width: 100vw; }
  }
  
  @media (max-width: 480px) {
    .grid { grid-template-columns: repeat(2, 1fr); gap: 12px; }
    .main { padding: 24px 12px 100px; }
    .card-img-wrap { aspect-ratio: 1 / 1; }
    .qty-ctrl button { width: 28px; }
    .btn-add { padding: 0 10px; font-size: 0.8rem; }
  }
</style>
</head>
<body>

<header>
  <div class="logo-container">
    <div class="logo"><img src="Logotipo - Andre Elias1.png" alt="André Elias Representações" /></div>
  </div>
  <button class="carrinho-btn" onclick="abrirCarrinho()">
    🛒 Ver Carrinho
    <span class="badge" id="badge">0</span>
  </button>
</header>

<div class="banner-loja">
  <img src="Logotipo - Andre Elias1.png" alt="André Elias Representações" class="banner-logo" />
  <div class="banner-texto">
    <div class="banner-titulo">Catálogo & Pedido de Espelhos</div>
    <div class="banner-sub">Monte seu pedido de forma simples: selecione os modelos, ajuste a quantidade desejada e envie diretamente para o nosso WhatsApp.</div>
  </div>
</div>

<div class="busca-wrap">
  <div class="busca-rel">
    <span class="busca-icon">🔍</span>
    <input type="text" id="busca" placeholder="Buscar por código ou medida (ex: 40x88)..." oninput="filtrar()" />
  </div>
</div>

<main class="main" id="main"></main>

<div class="overlay" id="overlay" onclick="fecharCarrinho()"></div>

<div class="carrinho-panel" id="painel">
  <div class="carrinho-header">
    <h2>🪞 Seu Pedido</h2>
    <button class="fechar-btn" onclick="fecharCarrinho()">✕</button>
  </div>
  <div class="carrinho-itens" id="itens-lista"></div>
  <div class="carrinho-footer">
    <div class="total-linha">
      <span class="total-label">Total do pedido</span>
      <span class="total-valor" id="total-val">R$ 0,00</span>
    </div>
    <input type="text" class="campo-nome" id="nome-cliente" placeholder="Digite seu nome completo" />
    <button class="btn-zap" onclick="enviarWhatsapp()">
      <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413z"/></svg>
      Enviar Pedido via WhatsApp
    </button>
  </div>
</div>

<script>
const SEU_WHATSAPP = "5513997324006";

const produtos = [
  { cod: "0058", nome: "Espelho 27×32 cm", desc: "Moldura preta, estilo moderno", preco: 20.24, img: "0058.png", multiplo: 10 },
  { cod: "1000", nome: "Espelho 33×43 cm", desc: "Moldura preta, acabamento fosco", preco: 28.93, img: "1000.png", multiplo: 10 },
  { cod: "5466", nome: "Espelho 39×63 cm", desc: "Moldura dourada trançada", preco: 39.35, img: "5466.png", multiplo: 10 },
  { cod: "9587", nome: "Espelho 40×88 cm", desc: "Moldura dourada trançada, corpo longo", preco: 62.00, img: "9587.png", multiplo: 5 },
  { cod: "9648", nome: "Espelho 44×123 cm", desc: "Moldura champagne trançada", preco: 86.79, img: "9648.png", multiplo: 1 },
  { cod: "9594", nome: "Espelho 50×150 cm", desc: "Moldura branca, espelho de chão", preco: 108.57, img: "9594.png", multiplo: 1 },
  { cod: "9150", nome: "Espelho 60×160 cm", desc: "Moldura prata trançada, espelho de chão", preco: 131.89, img: "9150.png", multiplo: 1 },
];

let carrinho = {};

function fmt(v) { return "R$ " + v.toFixed(2).replace(".", ","); }
function totalCarrinho() { return Object.values(carrinho).reduce((s, i) => s + i.preco * i.qty, 0); }
function qtdCarrinho() { return Object.values(carrinho).reduce((s, i) => s + i.qty, 0); }

function atualizarBadge() {
  const q = qtdCarrinho();
  document.getElementById("badge").textContent = q;
}

function addAoCarrinho(cod) {
  const p = produtos.find(x => x.cod === cod);
  if (!p) return;
  if (!carrinho[cod]) carrinho[cod] = { ...p, qty: 0 };
  carrinho[cod].qty += p.multiplo;
  atualizarBadge(); renderGrid(); renderCarrinho();
}

function removerDoCarrinho(cod) {
  if (!carrinho[cod]) return;
  const p = produtos.find(x => x.cod === cod);
  carrinho[cod].qty -= p.multiplo;
  if (carrinho[cod].qty <= 0) delete carrinho[cod];
  atualizarBadge(); renderGrid(); renderCarrinho();
}

let filtroBusca = "";
function filtrar() { filtroBusca = document.getElementById("busca").value.toLowerCase(); renderGrid(); }

function infoMultiplo(m) {
  if (m === 1) return "";
  return `<div class="info-multiplo">📦 Caixa fechada com ${m} un.</div>`;
}

function renderGrid() {
  const lista = filtroBusca
    ? produtos.filter(p => p.nome.toLowerCase().includes(filtroBusca) || p.cod.includes(filtroBusca) || p.desc.toLowerCase().includes(filtroBusca))
    : produtos;

  const main = document.getElementById("main");
  if (lista.length === 0) {
    main.innerHTML = `<p class="nenhum">Nenhum espelho encontrado para "<strong>${filtroBusca}</strong>".</p>`;
    return;
  }

  let html = `<div class="secao-titulo">Espelhos com Moldura</div><div class="grid">`;
  for (const p of lista) {
    const noCarr = carrinho[p.cod];
    const qty = noCarr ? noCarr.qty : 0;
    const precoLabel = p.multiplo > 1
      ? `${fmt(p.preco)} <span class="card-preco-unit">/ un.</span>`
      : fmt(p.preco);

    html += `
    <div class="card ${noCarr ? 'no-carrinho' : ''}">
      <div class="card-img-wrap">
        <img src="${p.img}" alt="${p.nome}" class="card-img" loading="lazy" />
      </div>
      <div class="card-body">
        <div class="card-cod">Cód. ${p.cod}</div>
        <div class="card-nome">${p.nome}</div>
        <div class="card-desc">${p.desc}</div>
        ${infoMultiplo(p.multiplo)}
        <div class="card-preco">${precoLabel}</div>
      </div>
      <div class="card-footer">
        <div class="footer-row">
          <div class="qty-ctrl">
            <button onclick="removerDoCarrinho('${p.cod}')">−</button>
            <span class="qty-val">${qty}</span>
            <button onclick="addAoCarrinho('${p.cod}')">+</button>
          </div>
          <button class="btn-add ${noCarr ? 'adicionado' : ''}" onclick="addAoCarrinho('${p.cod}')">
            ${noCarr ? '✓ No Carrinho' : '+ Adicionar'}
          </button>
        </div>
      </div>
    </div>`;
  }
  html += `</div>`;
  main.innerHTML = html;
}

function renderCarrinho() {
  const lista = document.getElementById("itens-lista");
  const total = document.getElementById("total-val");
  const itens = Object.values(carrinho);
  total.textContent = fmt(totalCarrinho());

  if (itens.length === 0) {
    lista.innerHTML = `<div class="carrinho-vazio"><div class="icone">🪞</div><p>Seu carrinho está vazio.<br>Adicione produtos para montar seu pedido.</p></div>`;
    return;
  }

  let html = "";
  for (const it of itens) {
    const multiInfo = it.multiplo > 1 ? `<span class="multiplo-info"> (Múltiplo de ${it.multiplo})</span>` : "";
    html += `
    <div class="item-cart">
      <img src="${it.img}" alt="${it.nome}" class="item-cart-img" />
      <div class="item-info">
        <div class="cod">Cód. ${it.cod}</div>
        <div class="nome">${it.nome}${multiInfo}</div>
        <div class="subtotal">${fmt(it.preco * it.qty)}</div>
      </div>
      <div class="item-cart-ctrl">
        <button class="mini-btn remover" onclick="removerDoCarrinho('${it.cod}')">
          ${it.qty <= it.multiplo ? '🗑️' : '−'}
        </button>
        <span class="item-qty-val">${it.qty}</span>
        <button class="mini-btn" onclick="addAoCarrinho('${it.cod}')">+</button>
      </div>
    </div>`;
  }
  lista.innerHTML = html;
}

function abrirCarrinho() {
  document.getElementById("painel").classList.add("aberto");
  document.getElementById("overlay").classList.add("ativo");
  renderCarrinho();
}
function fecharCarrinho() {
  document.getElementById("painel").classList.remove("aberto");
  document.getElementById("overlay").classList.remove("ativo");
}

function enviarWhatsapp() {
  const nome = document.getElementById("nome-cliente").value.trim();
  const itens = Object.values(carrinho);

  if (!nome) {
    const campo = document.getElementById("nome-cliente");
    campo.focus();
    campo.style.borderColor = "#EF4444";
    campo.placeholder = "⚠️ Digite seu nome completo primeiro";
    setTimeout(() => { campo.style.borderColor = ""; campo.placeholder = "Digite seu nome completo"; }, 2500);
    return;
  }
  if (itens.length === 0) return;

  let msg = `🪞 *PEDIDO DE ESPELHOS - ANDRÉ ELIAS REPRESENTAÇÕES*\n`;
  msg += `👤 *Cliente:* ${nome}\n`;
  msg += `📅 *Data:* ${new Date().toLocaleDateString("pt-BR")}\n\n`;
  msg += `*Itens Solicitados:*\n`;
  msg += `━━━━━━━━━━━━━━━━━━━━\n`;

  for (const it of itens) {
    const multipInfo = it.multiplo > 1 ? ` (cx c/ ${it.multiplo})` : "";
    msg += `📦 *Cód. ${it.cod}* - ${it.nome}${multipInfo}\n`;
    msg += `   Qtd: ${it.qty} un. × ${fmt(it.preco)} = *${fmt(it.preco * it.qty)}*\n\n`;
  }

  msg += `━━━━━━━━━━━━━━━━━━━━\n`;
  msg += `💰 *VALOR TOTAL: ${fmt(totalCarrinho())}*`;

  window.open(`https://wa.me/${SEU_WHATSAPP}?text=${encodeURIComponent(msg)}`, "_blank");
}

renderGrid();
</script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as file:
    file.write(html_content)
print("File 'index.html' created successfully.")