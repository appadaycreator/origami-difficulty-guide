# === 自動生成フィールド（編集不要）===
TITLE = '折り紙難易度ガイド【無料】完全ガイド'
DESCRIPTION = '作りたい折り紙の難易度判定と折り方のステップ解説。子供〜上級者まで対応。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '作りたい折り紙の難易度判定と折り方のステップ解説。子供〜上級者まで対応。'
COLOR1 = '#E0E7FF'
COLOR2 = '#F0F4FF'
COLOR_BTN = '#6366F1'
FOOTER_LINKS = [('https://appadaycreator.github.io/kids-activity-finder/', 'Kids Activity Finder'), ('https://appadaycreator.github.io/hobby-matcher/', 'Hobby Matcher')]

# ================================================================
# 以下の3フィールドを実装してください
# ================================================================
# ヒント:
#   - MAIN_HTML: class="card" を使ったUI、class="result" で結果を隠す
#   - JS_CODE: DOMContentLoadedで初期化、onclick or addEventListener を使う
#   - 結果表示: document.getElementById('result').classList.add('show')
#   - 色参照: CSS変数 var(--btn, #6366F1) または直接 #6366F1 を使用
#
# === MAIN_HTML サンプル ===
# MAIN_HTML = """
# <div class="card">
#   <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">⚡ タイトル</h2>
#   <label>入力項目</label>
#   <input type="number" id="val1" placeholder="数値を入力" min="0">
#   <button class="btn" style="margin-top:20px;" onclick="calc()">計算する</button>
#   <div class="result" id="result" style="margin-top:16px;">
#     <div class="card" style="text-align:center;">
#       <div id="output" style="font-size:2rem;font-weight:700;color:#6366F1;"></div>
#       <p id="msg" style="color:#666;font-size:14px;margin-top:8px;"></p>
#     </div>
#   </div>
# </div>
# """
# === JS_CODE サンプル ===
# JS_CODE = """
# document.addEventListener('DOMContentLoaded', () => {
#   document.getElementById('val1').addEventListener('keydown', e => {
#     if (e.key === 'Enter') calc();
#   });
# });
# function calc() {
#   const v = parseFloat(document.getElementById('val1').value);
#   if (isNaN(v) || v <= 0) { alert('正しい値を入力してください'); return; }
#   const result = v * 2; // 実際のロジックに置き換える
#   document.getElementById('output').textContent = result.toFixed(0);
#   document.getElementById('msg').textContent = '計算完了';
#   document.getElementById('result').classList.add('show');
# }
# """

CUSTOM_CSS = """"""

# ↓ スケルトンを参考に、サービス固有のUI・ロジックを実装してください
MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">🎴 折り紙難易度ガイド</h2>
  <!-- 設定入力をここに追加 -->

  <button class="btn" style="margin-top:20px;" onclick="generate()">作成する</button>
</div>
<div class="result" id="result" style="margin-top:16px;">
  <div class="card">
    <h3 style="font-size:15px;font-weight:700;margin-bottom:12px;color:#6366F1;">✅ 作成結果</h3>
    <div id="output"></div>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """// ★ここだけ実装（約10行）★
function getInputs(){{ // 変更: フォームから入力値を取得して検証
  const val=document.getElementById('val1')?.value||'';
  if(!val){{ alert('入力してください'); return null; }}
  return {{val}};
}}
function buildOutput(inputs){{ // 変更: 入力から結果HTMLを生成して返す
  return `<p>結果: ${{inputs.val}}</p>`; // 変更: 実際の出力
}}
// ★以下変更不要★
document.addEventListener('DOMContentLoaded',()=>{{}});
function generate(){{
  const inputs=getInputs(); if(!inputs) return;
  document.getElementById('output').innerHTML=buildOutput(inputs);
  document.getElementById('result').classList.add('show');
  document.getElementById('result').scrollIntoView({{behavior:'smooth',block:'start'}});
}}"""
