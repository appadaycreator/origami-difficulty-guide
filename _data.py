# === 自動生成フィールド（編集不要）===
TITLE = '折り紙難易度ガイド - 完全無料で使えるWebツール【登録不要】'
DESCRIPTION = '作りたい折り紙の難易度判定と折り方のステップ解説。子供〜上級者まで対応。登録不要・完全無料でご利用いただけます。'
DESCRIPTION_SHORT = '作りたい折り紙の難易度判定と折り方のステップ解説。子供〜上級者まで対応。'
COLOR1 = '#E0E7FF'
COLOR2 = '#F0F4FF'
COLOR_BTN = '#6366F1'
FOOTER_LINKS = [('https://appadaycreator.github.io/kids-activity-finder/', 'Kids Activity Finder'), ('https://appadaycreator.github.io/hobby-matcher/', 'Hobby Matcher')]

CUSTOM_CSS = """"""

# ↓ スケルトンを参考に、サービス固有のUI・ロジックを実装してください
MAIN_HTML = """<div class="card">
  <h2 style="font-size:18px;font-weight:700;margin-bottom:16px;">🦢 折り紙難易度・折り方ガイド</h2>
  <label>作りたい折り紙の種類</label>
  <select id="type">
    <option value="crane">鶴（ツル）</option>
    <option value="box">箱・入れ物</option>
    <option value="heart">ハート</option>
    <option value="flower">花（チューリップ・バラ）</option>
    <option value="shuriken">手裏剣・コマ</option>
    <option value="frog">カエル・飛ぶ昆虫</option>
    <option value="dragon">龍・複雑な動物</option>
    <option value="modular">ユニット折り紙（多面体）</option>
  </select>
  <label>経験レベル</label>
  <select id="exp">
    <option value="beginner">初心者（ほぼ初めて）</option>
    <option value="intermediate" selected>中級者（鶴は折れる）</option>
    <option value="advanced">上級者（複雑な作品も挑戦済み）</option>
  </select>
  <button class="btn" style="margin-top:20px;" onclick="generate()">難易度・折り方を確認</button>
</div>
<div class="result" id="result" style="margin-top:16px;">
  <div class="card">
    <h3 style="font-size:15px;font-weight:700;margin-bottom:12px;color:#6366F1;">📋 折り紙ガイド</h3>
    <div id="output"></div>
  </div>
</div>"""

# JS: スタブの TODO コメント箇所を実装してください（骨格は変えないこと）
JS_CODE = """const ORIGAMI = {
  crane: { name:'鶴（ツル）', level:3, steps:15, time:'15〜20分', size:'15cm×15cm', emoji:'🦢', desc:'日本の折り紙の代表作。基本の「鳥の基本形」から作られます。', tips:['折り目を先につけておくと折りやすい','尾と首の引っ張り具合で形が変わる','100羽折ると「折り鶴千羽鶴」に！'], refs:['YouTube「折り紙鶴 折り方」で多数動画あり'] },
  box: { name:'箱・入れ物', level:2, steps:12, time:'10〜15分', size:'15cm×15cm（2枚）', emoji:'📦', desc:'ふたと本体の2枚で作る実用的な箱。プレゼントの小箱にも使えます。', tips:['ふたは本体より0.5cm大きい紙を使う','折り目を丁寧につけると角がきれいになる','模様入りの紙を使うと見栄えが良い'], refs:['折り紙パーティー「折り紙箱」で検索'] },
  heart: { name:'ハート', level:2, steps:10, time:'5〜10分', size:'正方形の紙なら何でも', emoji:'❤️', desc:'バレンタインや手紙のアクセントに。簡単な割に仕上がりがきれい。', tips:['折り紙の裏側が表になる場合が多い','小さめ（7.5cm）で作ってメッセージカードに','連続して作ってガーランドにも'], refs:['「折り紙 ハート 簡単」で検索'] },
  flower: { name:'花（チューリップ・バラ）', level:4, steps:20, time:'20〜30分', size:'15cm×15cm', emoji:'🌹', desc:'難易度はやや高め。チューリップは比較的簡単、バラは上級。', tips:['バラはカワサキローズが有名（上級向け）','チューリップは2パーツ（花と葉）で作る','花びらを少し外側に広げると立体感が出る'], refs:['「川崎ローズ 折り方」「折り紙チューリップ」で検索'] },
  shuriken: { name:'手裏剣・コマ', level:2, steps:16, time:'10分（2枚使用）', size:'15cm×15cm（2枚）', emoji:'⭐', desc:'2枚の紙を組み合わせて作る。子供に大人気の作品。', tips:['2枚の色を変えるとカラフルになる','しっかり押し込むと外れにくくなる','実際に投げて遊べる（屋内で）'], refs:['「折り紙 手裏剣 2枚」で検索'] },
  frog: { name:'カエル・飛ぶ昆虫', level:4, steps:25, time:'20〜30分', size:'15cm×15cm', emoji:'🐸', desc:'おしりを押すとぴょんと飛ぶカエルが定番。動く折り紙として人気。', tips:['カエルのジャンプ力は紙の硬さで変わる','後ろ足の折り方が飛び方のポイント','バッタ・セミなど昆虫系も同難易度'], refs:['「折り紙 カエル ぴょんぴょん」で検索'] },
  dragon: { name:'龍・複雑な動物', level:5, steps:50, time:'1〜3時間', size:'30cm×30cm以上推奨', emoji:'🐉', desc:'上級者向けの複雑作品。竹尾・Satoshi Kamiyaなどの作品が有名。', tips:['ウェットフォールディング（湿らせて形づくり）が効果的','薄くて丈夫な和紙（障子紙等）を推奨','折り図は専門書・Orizuru（折り鶴）系サイトで'], refs:['「神谷哲史 龍 折り方」で検索・専門書推奨'] },
  modular: { name:'ユニット折り紙（多面体）', level:4, steps:30, time:'1〜2時間（30パーツ）', size:'7.5cm×7.5cm（多数）', emoji:'⭐', desc:'同じパーツを複数作って組み合わせる。立体的で美しい。', tips:['ソノベキューブ（6枚）・星型（30枚）が入門','パーツをしっかり折ると組みやすい','色違いのパーツを組み合わせるとカラフルに'], refs:['「ソノベキューブ 折り方」「ユニット折り紙 星」で検索'] },
};
const LEVEL_MAP = { beginner:[1,2], intermediate:[2,3,4], advanced:[3,4,5] };
function getInputs() {
  return { type: document.getElementById('type').value, exp: document.getElementById('exp').value };
}
function buildOutput(inputs) {
  const o = ORIGAMI[inputs.type];
  const levels = LEVEL_MAP[inputs.exp];
  const diff = o.level;
  const stars = '★'.repeat(diff) + '☆'.repeat(5-diff);
  let advice = '';
  if(diff <= levels[0]) advice = '✅ あなたのレベルにちょうど良い作品です！';
  else if(diff <= levels[1]) advice = '💪 少し挑戦的ですが十分挑戦できます！';
  else advice = '⚠️ やや難しめです。まず簡単な作品で練習してから挑戦しましょう。';
  const tipsHtml = o.tips.map(t=>`<li style="margin-bottom:5px;">${t}</li>`).join('');
  return `<div style="background:#eff6ff;border-radius:10px;padding:16px;margin-bottom:14px;">
    <div style="font-size:24px;margin-bottom:8px;">${o.emoji}</div>
    <div style="font-size:18px;font-weight:700;color:#1e40af;margin-bottom:4px;">${o.name}</div>
    <div style="font-size:20px;color:#f59e0b;margin-bottom:8px;">${stars}</div>
    <div style="font-size:13px;color:#374151;line-height:2;">
      📝 手順数: 約${o.steps}ステップ<br>
      ⏱️ 所要時間: ${o.time}<br>
      📏 推奨サイズ: ${o.size}
    </div>
  </div>
  <div style="font-size:13px;color:#374151;margin-bottom:12px;">💬 ${o.desc}</div>
  <div style="font-size:13px;font-weight:600;margin-bottom:4px;">${advice}</div>
  <div style="font-size:13px;font-weight:600;color:#374151;margin:12px 0 6px;">💡 成功のコツ</div>
  <ul style="padding-left:18px;font-size:13px;color:#475569;line-height:1.9;">${tipsHtml}</ul>
  <div style="background:#fafafa;border-radius:8px;padding:10px;margin-top:10px;font-size:12px;color:#6b7280;">
    🔍 参考: ${o.refs.join(' / ')}
  </div>`;
}
document.addEventListener('DOMContentLoaded',()=>{});
function generate() {
  const inputs = getInputs();
  document.getElementById('output').innerHTML = buildOutput(inputs);
  document.getElementById('result').classList.add('show');
  document.getElementById('result').scrollIntoView({behavior:'smooth',block:'start'});
}"""

FAQ = [
    ("折り紙難易度ガイドは無料で使えますか？", "はい、完全無料・登録不要でご利用いただけます。"),
    ("何回でも使えますか？", "はい、回数制限なく何度でもご利用いただけます。"),
    ("入力したデータはサーバーに送信されますか？", "いいえ。すべての処理はブラウザ内で完結し、入力内容はサーバーへ送信されません。"),
    ("スマートフォンでも使えますか？", "はい、スマートフォン・タブレット・PCすべてに最適化されています。"),
    ("結果を保存・共有できますか？", "スクリーンショットでの保存またはSNSシェアボタンからご共有いただけます。"),
]

HOW_TO = [
    "ページを開き、入力フォームの項目を確認する",
    "必要な情報を入力または選択する",
    "実行ボタンをクリックして結果を取得する",
    "表示された結果・アドバイスを確認する",
    "必要に応じてコピー・SNSシェアで活用する",
]

FOOTER_LINKS = [('https://appadaycreator.github.io/kids-activity-finder/', 'Kids Activity Finder'), ('https://appadaycreator.github.io/hobby-matcher/', 'Hobby Matcher'), ('https://appadaycreator.com/sleep-quality-checker/', '睡眠の質チェッカー')]

