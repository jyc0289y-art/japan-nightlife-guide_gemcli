#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
두 가지 테마 HTML 생성:
  1. 표준 v3 (용어 순화 + YouTube 썸네일 수정)
  2. HOBIS 테마 (스타크래프트 테란 감성)
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from make_guide_v3 import (
    CITY_DATA, CITY_ORDER, COST_TABLE,
    NANPA_STRATEGIES, NANPA_TIPS,
    SCAM_PREVENTION, HANAMI_STRATEGY, ESSENTIAL_APPS,
)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ────────────────────────────────────────────────────────────
#  공통 데이터 헬퍼
# ────────────────────────────────────────────────────────────

def yt_thumb(yt_id, title, channel, note, url):
    """YouTube 썸네일 + 외부 링크 블록 (embed 대신)"""
    return f"""
<div class="yt-thumb-wrap">
  <a href="{url}" target="_blank" rel="noopener noreferrer">
    <img
      src="https://img.youtube.com/vi/{yt_id}/hqdefault.jpg"
      alt="{title}"
      onerror="this.src='https://img.youtube.com/vi/{yt_id}/mqdefault.jpg'"
    >
    <div class="play-overlay">
      <span class="play-icon">▶</span>
      <span class="play-text">유튜브에서 시청</span>
    </div>
  </a>
</div>
<p class="yt-meta">📺 <a href="{url}" target="_blank">{title}</a> — {channel}</p>
<p class="yt-note">💡 {note}</p>
"""

def eval_data():
    return [
        ("후쿠오카",   "★★★☆☆", "접근성·가격 최고. 한국인 많아 희소성 낮음."),
        ("미야자키",   "★★★★★", "스낵바 밀도 전국 1위. 현지인 비율 최고. 최우선 추천."),
        ("가고시마",   "★★★★☆", "쇼추 문화 공유로 대화 쉬움. 사쿠라지마 화제 풍부."),
        ("오이타/벳부","★★★☆☆", "온천 후 이자카야 황금 루트."),
        ("구마모토",   "★★★★☆", "쿠마몬 화제 최강. 성 야경 데이트 활용 가능."),
        ("나가사키",   "★★★★☆", "이국적 분위기. 야경 세계 3대 데이트 카드."),
        ("나하",       "★★★★☆", "아열대 리조트 기분. 우치나구치 즉각 반응."),
        ("기타큐슈",   "★★★★☆", "외국인 희소성 극대화. 야키토리 화제."),
        ("히로시마",   "★★★★☆", "역사 감동 공유. 나가레카와 규모 크고 인터내셔널."),
        ("오카야마",   "★★★★☆", "외국인 거의 없음. ぼっけぇ 방언 임팩트."),
        ("마쓰야마",   "★★★☆☆", "온천 후 이자카야 루트. 도고 온천 화제."),
        ("삿포로",     "★★★★☆", "스스키노 규모 압도적. 클럽 가능."),
        ("하코다테",   "★★★☆☆", "야경 데이트 최적. 유흥가 규모 소규모."),
        ("센다이",     "★★★★☆", "도호쿠 최대 유흥가. おばんです 인사 강력."),
        ("가나자와",   "★★★☆☆", "'작은 교토' 세련된 분위기. 해산물 화제."),
    ]

CONCLUSION = [
    "【최우선 추천】 미야자키: 스낵바 밀도 전국 1위, 현지인 비율 최고, 방언 효과 극대화.",
    "【차선 추천 (규슈)】 가고시마·구마모토·나가사키·기타큐슈: 어느 도시든 그대로 적용 가능.",
    "【하나미 활용】 4월 초 규슈·주고쿠 최적. 벚꽃 낮 → 이자카야 저녁 2단계 플랜 성공률 최고.",
    "【예산 최적화】 기타큐슈·미야자키: 동일 효과 + 상대적으로 저렴한 항공권·물가.",
    "【최종 제안】 4박 5일 단일 도시 집중: 미야자키 또는 가고시마 → 이틀째부터 동네 단골 효과.",
]


# ════════════════════════════════════════════════════════════════
#  표준 v3 HTML (용어 순화 + YouTube 썸네일)
# ════════════════════════════════════════════════════════════════

def build_html_v3():

    nav_items = "".join(
        f'<li><a href="#{ck}">{CITY_DATA[ck]["flag"]} {CITY_DATA[ck]["name_ko"]}</a></li>\n'
        for ck in CITY_ORDER
    )
    cost_rows = "".join(
        f"<tr><td>{i}</td><td class='cost'>{c}</td><td>{d}</td></tr>\n"
        for i, c, d in COST_TABLE
    )
    strategy_rows = "".join(
        f"<tr><td><b>{p}</b></td><td>{s}</td></tr>\n"
        for p, s in NANPA_STRATEGIES
    )
    tips_rows = "".join(
        f"<tr><td>{si}</td><td class='jp'>{ex}</td><td>{d}</td></tr>\n"
        for si, ex, d in NANPA_TIPS
    )
    scam_html = "".join(
        f"<div class='tip-card'><b>▶ {t}</b><p>{d}</p></div>\n"
        for t, d in SCAM_PREVENTION
    )
    hanami_html = "".join(
        f"<div class='tip-card sakura'><b>🌸 {t}</b><p>{d}</p></div>\n"
        for t, d in HANAMI_STRATEGY
    )
    apps_html = "".join(
        f"<div class='app-card'><span class='app-name'>📲 {n}</span><span class='app-desc'>{d}</span></div>\n"
        for n, d in ESSENTIAL_APPS
    )
    eval_rows = ""
    for c, s, cm in eval_data():
        sc = "five" if "★★★★★" in s else ("four" if "★★★★☆" in s else "three")
        eval_rows += f"<tr><td><b>{c}</b></td><td class='score {sc}'>{s}</td><td>{cm}</td></tr>\n"

    # 도시별 섹션
    city_sections = ""
    for ck in CITY_ORDER:
        cd = CITY_DATA[ck]
        yt = cd["youtube_dialect"]
        yt_url = f"https://youtu.be/{yt['id']}"
        thumb_html = yt_thumb(yt['id'], yt['title'], yt['channel'], yt['note'], yt_url)

        tt_rows = "".join(
            f"<tr><td class='time'>{t}</td><td><b>{a}</b></td><td class='tip-text'>{tip}</td></tr>\n"
            for t, a, tip in cd["timetable"]
        )
        cs_rows = "".join(
            f"<tr><td>{s}</td><td class='jp dialogue'>{l}</td><td class='note'>{n}</td></tr>\n"
            for s, l, n in cd["conversation_script"]
        )
        spots_html = "".join(
            f"<div class='spot-card'><span class='spot-name'>{sn}</span><span class='spot-rating'>{sr}</span><p>{sd}</p></div>\n"
            for sn, sr, sd in cd["spots"]
        )
        daytime_html = "".join(
            f"<div class='day-item'><b>▶ {dn}</b><p>{dd}</p></div>\n"
            for dn, dd in cd["daytime"]
        )
        d_name, d_order, d_brand = cd["local_drink"]
        s_spot, s_time, s_tip = cd["sakura"]

        city_sections += f"""
<section class="city-section" id="{ck}">
  <div class="city-header">
    <h2>{cd['flag']} {cd['name_ko']} <span class="name-jp">({cd['name_jp']})</span>
        <span class="region-badge">{cd['region']}</span></h2>
    <p class="tagline">『{cd['tagline']}』</p>
  </div>
  <div class="city-grid">
    <div class="city-col-main">

      <div class="info-block">
        <h3>✈️ 항공편</h3>
        <p>{cd['flight']}</p>
        <p class="sub">ℹ️ {cd['flight_note']}</p>
        <p class="sub">🚌 공항→시내: {cd['access']}</p>
      </div>

      <div class="info-block youtube-block">
        <h3>📺 방언 학습 YouTube</h3>
        {thumb_html}
      </div>

      <div class="info-block nanpa-block">
        <h3>🍻 유흥가 &amp; 방언 접근 전략</h3>
        <p><b>📍 핵심 구역:</b> {cd['district']}</p>
        <p class="sub">{cd['district_desc']}</p>
        <div class="score-bar">
          <span class="label">⭐ 적합도:</span>
          <span class="score-stars">{cd['nanpa_score']}</span>
        </div>
        <p><b>🎯 이유:</b> {cd['nanpa_reason']}</p>
        <p class="dialect-badge">🗣️ {cd['nanpa_dialect']}</p>
        <div class="strategy-box">
          <b>💡 핵심 전략</b>
          <p>{cd['nanpa_strategy']}</p>
        </div>
      </div>

      <div class="info-block timetable-block">
        <h3>⏰ 야간 동선 타임테이블</h3>
        <table class="data-table">
          <thead><tr><th>시간</th><th>활동</th><th>팁</th></tr></thead>
          <tbody>{tt_rows}</tbody>
        </table>
      </div>

      <div class="info-block script-block">
        <h3>💬 실전 대화 스크립트</h3>
        <table class="data-table">
          <thead><tr><th>상황</th><th>일본어 대사</th><th>해설</th></tr></thead>
          <tbody>{cs_rows}</tbody>
        </table>
      </div>

    </div>
    <div class="city-col-side">

      <div class="info-block drink-block">
        <h3>🍶 지역 술</h3>
        <p class="drink-name">{d_name}</p>
        <p class="order-phrase jp">{d_order}</p>
        <p class="sub">추천: {d_brand}</p>
      </div>

      <div class="info-block sakura-block">
        <h3>🌸 벚꽃 &amp; 하나미</h3>
        <p><b>{s_spot}</b></p>
        <p class="sub">⏰ 개화: {s_time}</p>
        <p>{s_tip}</p>
      </div>

      <div class="info-block daytime-block">
        <h3>☀️ 낮 일정</h3>
        {daytime_html}
      </div>

      <div class="info-block spots-block">
        <h3>🍺 추천 이자카야 &amp; 바</h3>
        {spots_html}
      </div>

      <div class="info-block food-block">
        <h3>🍽️ 명물 음식</h3>
        <p class="food-name">{cd['food_name']}</p>
        <p>{cd['food_desc']}</p>
      </div>

      <div class="info-block budget-block">
        <h3>🏨 숙박 &amp; 예산</h3>
        <p>{cd.get('accommodation_detail', cd['accommodation'])}</p>
        <div class="budget-box">
          <p>💰 <b>2인 총 예산:</b> {cd['budget_2pax']}</p>
          <p>💰 <b>1인 1일:</b> {cd['budget_1p_day']}</p>
        </div>
      </div>

    </div>
  </div>
</section>"""

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>🎯 일본 소도시 나이트라이프 가이드 v3</title>
<style>
:root{{--red:#b41e1e;--navy:#142278;--green:#145432;--orange:#a05000;--purple:#500878;--pink:#b43c78;--bg:#f8f9fb;--card:#fff;--border:#dde0e8;--text:#1a1a2e;}}
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{font-family:'Apple SD Gothic Neo','Noto Sans KR',sans-serif;background:var(--bg);color:var(--text);font-size:14px;line-height:1.6;}}
.main-header{{background:linear-gradient(135deg,var(--navy) 0%,var(--red) 100%);color:#fff;padding:32px;}}
.main-header h1{{font-size:22px;margin-bottom:6px;}}
.main-header .subtitle{{font-size:13px;opacity:.85;}}
.main-header .meta{{margin-top:8px;font-size:12px;opacity:.75;}}
.layout{{display:flex;min-height:100vh;}}
.sidebar{{width:195px;min-width:195px;background:var(--navy);color:#fff;position:sticky;top:0;height:100vh;overflow-y:auto;padding:12px 0;}}
.sidebar h3{{font-size:10px;text-transform:uppercase;letter-spacing:1px;padding:8px 14px;opacity:.55;}}
.sidebar ul{{list-style:none;}}
.sidebar li a{{display:block;padding:7px 14px;color:rgba(255,255,255,.8);text-decoration:none;font-size:12px;border-left:3px solid transparent;transition:all .2s;}}
.sidebar li a:hover{{background:rgba(255,255,255,.1);border-left-color:#fff;color:#fff;}}
.main-content{{flex:1;padding:22px 26px;max-width:1080px;}}
.section-card{{background:var(--card);border-radius:12px;border:1px solid var(--border);padding:24px;margin-bottom:22px;box-shadow:0 2px 8px rgba(0,0,0,.06);}}
.section-card h2{{font-size:19px;color:var(--red);margin-bottom:14px;padding-bottom:8px;border-bottom:2px solid var(--red);}}
.section-card h3{{font-size:14px;color:var(--navy);margin:14px 0 7px;}}
.tip-card{{background:#fff8f0;border-left:4px solid var(--orange);padding:11px 14px;margin-bottom:9px;border-radius:0 7px 7px 0;}}
.tip-card.sakura{{background:#fff0f6;border-left-color:var(--pink);}}
.tip-card b{{display:block;margin-bottom:3px;font-size:12px;}}
.tip-card p{{font-size:11px;color:#444;}}
.app-card{{display:flex;align-items:flex-start;gap:8px;padding:7px 11px;margin-bottom:5px;background:#f0f4ff;border-radius:6px;}}
.app-name{{font-weight:700;font-size:12px;min-width:180px;color:var(--navy);}}
.app-desc{{font-size:11px;color:#444;}}
.city-section{{background:var(--card);border-radius:13px;border:1px solid var(--border);margin-bottom:28px;overflow:hidden;box-shadow:0 4px 14px rgba(0,0,0,.07);}}
.city-header{{background:linear-gradient(135deg,var(--navy) 0%,#1e3a8a 100%);color:#fff;padding:20px 26px;}}
.city-header h2{{font-size:20px;margin-bottom:3px;}}
.name-jp{{font-size:14px;opacity:.8;}}
.region-badge{{font-size:10px;background:rgba(255,255,255,.2);padding:2px 9px;border-radius:20px;margin-left:7px;}}
.tagline{{font-size:13px;opacity:.85;margin-top:3px;font-style:italic;}}
.city-grid{{display:grid;grid-template-columns:2fr 1fr;}}
.city-col-main{{padding:18px;border-right:1px solid var(--border);}}
.city-col-side{{padding:18px;background:#f9fafc;}}
.info-block{{margin-bottom:18px;padding-bottom:14px;border-bottom:1px solid var(--border);}}
.info-block:last-child{{border-bottom:none;margin-bottom:0;}}
.info-block h3{{font-size:13px;color:var(--navy);font-weight:700;margin-bottom:9px;}}
.info-block p{{font-size:12px;margin-bottom:3px;}}
.info-block .sub{{font-size:11px;color:#666;}}
/* YouTube 썸네일 */
.youtube-block{{background:#0d0d1e;border-radius:8px;padding:14px;color:#fff;}}
.youtube-block h3{{color:#ff6b6b;}}
.yt-thumb-wrap{{position:relative;margin:10px 0;border-radius:8px;overflow:hidden;cursor:pointer;}}
.yt-thumb-wrap img{{width:100%;display:block;border-radius:8px;}}
.play-overlay{{position:absolute;top:0;left:0;width:100%;height:100%;background:rgba(0,0,0,.35);display:flex;flex-direction:column;align-items:center;justify-content:center;opacity:0;transition:.2s;border-radius:8px;}}
.yt-thumb-wrap:hover .play-overlay{{opacity:1;}}
.play-icon{{font-size:42px;color:#fff;line-height:1;}}
.play-text{{color:#fff;font-size:12px;margin-top:6px;font-weight:700;}}
.yt-meta{{font-size:11px;color:#aaa;}}
.yt-meta a{{color:#7ab3ff;}}
.yt-note{{font-size:10px;color:#888;margin-top:4px;}}
/* 접근 전략 */
.nanpa-block{{background:#fff5f5;border-radius:8px;padding:14px;}}
.score-bar{{display:flex;align-items:center;gap:10px;margin:7px 0;}}
.score-stars{{font-size:15px;color:#f0a000;}}
.dialect-badge{{background:var(--purple);color:#fff;padding:3px 11px;border-radius:20px;font-size:11px;display:inline-block;margin:5px 0;}}
.strategy-box{{background:#fff;border-left:4px solid var(--red);padding:9px 13px;margin-top:9px;border-radius:0 6px 6px 0;}}
.strategy-box b{{display:block;margin-bottom:3px;color:var(--red);font-size:12px;}}
/* 테이블 */
.data-table{{width:100%;border-collapse:collapse;font-size:11px;margin-top:7px;}}
.data-table th{{background:var(--navy);color:#fff;padding:6px 9px;text-align:left;font-size:10px;}}
.data-table td{{padding:6px 9px;border-bottom:1px solid var(--border);vertical-align:top;}}
.data-table tr:nth-child(even) td{{background:#f8f9fb;}}
.data-table .time{{color:var(--orange);font-weight:700;white-space:nowrap;font-size:10px;}}
.data-table .tip-text{{color:#666;font-size:10px;}}
.data-table .jp{{color:var(--navy);font-family:serif;}}
.data-table .dialogue{{font-family:serif;font-size:11px;}}
.data-table .note{{font-size:10px;color:#555;}}
/* 사이드 블록 */
.drink-block{{background:#f0f8ff;border-radius:8px;padding:13px;}}
.drink-name{{font-size:14px;font-weight:700;color:var(--navy);}}
.order-phrase{{color:var(--purple);font-family:serif;margin:5px 0;}}
.sakura-block{{background:#fff0f8;border-radius:8px;padding:13px;}}
.day-item{{margin-bottom:9px;}}
.day-item b{{font-size:12px;color:var(--navy);display:block;}}
.day-item p{{font-size:11px;color:#555;}}
.spot-card{{border:1px solid var(--border);border-radius:7px;padding:9px 11px;margin-bottom:7px;background:#fff;}}
.spot-name{{font-weight:700;font-size:12px;display:block;}}
.spot-rating{{font-size:10px;color:#f0a000;display:block;margin-bottom:3px;}}
.spot-card p{{font-size:11px;color:#555;}}
.food-block{{background:#fffaf0;border-radius:8px;padding:13px;}}
.food-name{{font-size:14px;font-weight:700;color:var(--orange);margin-bottom:5px;}}
.budget-block{{background:#f0fff4;border-radius:8px;padding:13px;}}
.budget-box p{{font-size:11px;margin-bottom:3px;}}
/* 평가 */
.score.five{{color:#b41e1e;font-size:14px;}}
.score.four{{color:#e07000;font-size:14px;}}
.score.three{{color:#777;font-size:14px;}}
.formula-box{{background:linear-gradient(135deg,#1a1a4e 0%,#3a0060 100%);color:#fff;border-radius:10px;padding:18px 22px;margin:14px 0;}}
.formula-box .formula{{font-size:13px;font-weight:700;color:#7df;}}
.conclusion-box{{background:linear-gradient(135deg,#b41e1e 0%,#a05000 100%);color:#fff;border-radius:10px;padding:18px 22px;margin:14px 0;}}
.conclusion-box li{{margin-bottom:7px;font-size:12px;}}
table.common-table{{width:100%;border-collapse:collapse;font-size:12px;margin:10px 0;}}
table.common-table th{{background:var(--navy);color:#fff;padding:8px 11px;text-align:left;}}
table.common-table td{{padding:7px 11px;border-bottom:1px solid var(--border);}}
table.common-table tr:hover td{{background:#f0f4ff;}}
.cost{{font-weight:700;color:var(--red);white-space:nowrap;}}
@media(max-width:900px){{.city-grid{{grid-template-columns:1fr;}}.city-col-main{{border-right:none;border-bottom:1px solid var(--border);}}.sidebar{{display:none;}}}}
@media print{{.sidebar{{display:none;}}.main-header{{position:static;}}.city-section{{page-break-before:always;}}.yt-thumb-wrap{{display:none;}}}}
</style>
</head>
<body>
<header class="main-header">
  <h1>🎯 일본 소도시 나이트라이프 가이드 v3</h1>
  <div class="subtitle">ICN 직항 15개 소도시 | 이자카야·스낵바 완전 공략 | 방언 접근 전략 | 목적달성 플랜</div>
  <div class="meta">📅 2026년 4월 첫째 주 4박5일 | 👥 일본어 능숙 한국 남성 2인 | 🎯 이자카야·스낵바 현지 여성 인연 만들기</div>
</header>
<div class="layout">
  <nav class="sidebar">
    <h3>목차</h3>
    <ul>
      <li><a href="#strategy">📋 전략 총론</a></li>
      <li><a href="#tactics">🎯 핵심 전략</a></li>
      <li><a href="#scam">🚫 바가지 방지</a></li>
      <li><a href="#hanami">🌸 하나미 활용</a></li>
      <li><a href="#cost">💴 비용 가이드</a></li>
      <li><a href="#apps">📱 필수 앱</a></li>
      <li><a href="#cities">🗺️ 도시별 플랜</a></li>
      {nav_items}
      <li><a href="#eval">📊 종합 평가</a></li>
    </ul>
  </nav>
  <main class="main-content">

    <section class="section-card" id="strategy">
      <h2>📋 전략 총론 — 목적과 활용법</h2>
      <div class="formula-box">
        <p class="formula">✅ 성공 공식: 방언 한 마디 → 관심 유도 → 합석 → 대화 심화 → LINE 교환 → 다음 자리 제안</p>
      </div>
      <h3>📌 활용 순서</h3>
      <ol style="padding-left:20px;line-height:2;font-size:13px">
        <li><b>출발 2주 전</b> — 방언 YouTube 시청. 핵심 표현 3개씩 암기</li>
        <li><b>출발 1주 전</b> — 도시 섹션 정독. 타임테이블·대화 스크립트 숙지</li>
        <li><b>현지 도착 당일</b> — 타임테이블 따라 이자카야 진입. 방언 첫 마디 준비</li>
        <li><b>야간 활동 중</b> — 대화 스크립트 참고. 자연스럽게 단계별 진행</li>
        <li><b>LINE 교환 후</b> — 귀국 후에도 연락 유지. 다음 방문 약속</li>
      </ol>
      <h3>⚠️ 주의사항</h3>
      <ul style="padding-left:20px;font-size:12px;line-height:2">
        <li>항공 가격은 2026.03 기준 — 실제 예약 시 항공사 공식 사이트 재확인 필수</li>
        <li>스낵바 입장료·세트는 가게마다 편차 큼 — 입장 전 반드시 직접 확인</li>
        <li>4월 첫째 주는 골든위크 직전 — 호텔 가격 상승 주의</li>
        <li>벚꽃 개화 시기 매년 변동 — 여행 직전 sakura.info 실시간 확인</li>
      </ul>
    </section>

    <section class="section-card" id="tactics">
      <h2>🎯 핵심 전략 가이드</h2>
      <h3>🏠 장소별 접근 전략</h3>
      <table class="common-table">
        <thead><tr><th>장소 유형</th><th>접근 전략</th></tr></thead>
        <tbody>{strategy_rows}</tbody>
      </table>
      <h3 style="margin-top:18px">⏰ 시간대별 전략</h3>
      <table class="common-table">
        <thead><tr><th>시간대</th><th>전략</th></tr></thead>
        <tbody>
          <tr><td class="time">17:00~19:00 (골든 타임)</td><td>밥집·야타이 1차. 퇴근 후 첫 술자리. 자연스러운 첫 접촉 최적.</td></tr>
          <tr><td class="time">19:00~21:00 (황금 타임)</td><td>이자카야 메인 시간대. 분위기 무르익음. 합석·대화 성공률 최고.</td></tr>
          <tr><td class="time">21:00~23:00 (기회 시간)</td><td>스낵바·바 2차. 경계심 낮아진 상태 — 대화 진입 용이.</td></tr>
          <tr><td class="time">23:00~02:00 (심야)</td><td>클럽·심야 바. LINE 교환 또는 3차 제안 마지막 기회.</td></tr>
        </tbody>
      </table>
      <h3 style="margin-top:18px">💬 범용 대화 스크립트</h3>
      <table class="common-table">
        <thead><tr><th>상황</th><th>일본어 표현</th><th>해설</th></tr></thead>
        <tbody>{tips_rows}</tbody>
      </table>
    </section>

    <section class="section-card" id="scam">
      <h2>🚫 바가지 방지 완전 가이드</h2>
      {scam_html}
    </section>

    <section class="section-card" id="hanami">
      <h2>🌸 4월 하나미 활용 전략</h2>
      {hanami_html}
    </section>

    <section class="section-card" id="cost">
      <h2>💴 비용 완전 가이드</h2>
      <table class="common-table">
        <thead><tr><th>항목</th><th>비용</th><th>설명</th></tr></thead>
        <tbody>{cost_rows}</tbody>
      </table>
      <div style="background:#e8f5e9;border-radius:8px;padding:12px;margin-top:14px;font-size:13px">
        💡 <b>2인 4박 5일 총 예산: ¥300,000~600,000 (1인 ¥150,000~300,000)</b><br>
        <span style="font-size:11px;color:#555">항공권이 전체의 40~50% → 조기 예약이 핵심 절약 포인트</span>
      </div>
    </section>

    <section class="section-card" id="apps">
      <h2>📱 필수 앱 목록</h2>
      {apps_html}
    </section>

    <div id="cities" style="margin:28px 0 6px">
      <h2 style="font-size:20px;color:var(--red);border-bottom:3px solid var(--red);padding-bottom:9px">
        🗺️ 도시별 여행 플랜 (15개 도시)
      </h2>
      <p style="font-size:12px;color:#555;margin-top:7px">
        각 도시: 항공편 → 방언 YouTube → 접근 전략 → 야간 타임테이블 → 지역술 → 벚꽃 → 낮 일정 → 추천 스팟 → 대화 스크립트 → 숙박 &amp; 예산
      </p>
    </div>

    {city_sections}

    <section class="section-card" id="eval">
      <h2>📊 종합 평가 &amp; 총평</h2>
      <table class="common-table">
        <thead><tr><th>도시</th><th>적합도</th><th>평가</th></tr></thead>
        <tbody>{eval_rows}</tbody>
      </table>
      <h3 style="margin-top:22px">🏆 총평 &amp; 결론</h3>
      <div class="conclusion-box">
        <ul style="padding-left:18px">
          {''.join(f'<li>{l}</li>' for l in CONCLUSION)}
        </ul>
      </div>
      <p style="font-size:11px;color:#888;margin-top:18px;text-align:center">
        📌 일본 문화와 이자카야 예절을 존중하는 범위 내에서 활용하시기 바랍니다.
      </p>
    </section>
  </main>
</div>
</body>
</html>"""

    out = os.path.join(BASE_DIR, "20260401_일본나이트라이프가이드_v3.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ 표준 v3 HTML 저장: {out}  ({os.path.getsize(out)//1024}KB)")
    return out


# ════════════════════════════════════════════════════════════════
#  HOBIS 테마 HTML (스타크래프트 테란 감성)
# ════════════════════════════════════════════════════════════════

def build_html_hobis():

    nav_items = "".join(
        f'<li><a href="#{ck}">{CITY_DATA[ck]["flag"]} {CITY_DATA[ck]["name_ko"].upper()}</a></li>\n'
        for ck in CITY_ORDER
    )
    cost_rows = "".join(
        f"<tr><td>{i}</td><td class='hl'>{c}</td><td>{d}</td></tr>\n"
        for i, c, d in COST_TABLE
    )
    strategy_rows = "".join(
        f"<tr><td class='hl'>{p}</td><td>{s}</td></tr>\n"
        for p, s in NANPA_STRATEGIES
    )
    tips_rows = "".join(
        f"<tr><td>{si}</td><td class='jp-h'>{ex}</td><td>{d}</td></tr>\n"
        for si, ex, d in NANPA_TIPS
    )
    scam_html = "".join(
        f"<div class='h-card'><div class='h-card-title'>{t}</div><p>{d}</p></div>\n"
        for t, d in SCAM_PREVENTION
    )
    hanami_html = "".join(
        f"<div class='h-card sakura-h'><div class='h-card-title'>🌸 {t}</div><p>{d}</p></div>\n"
        for t, d in HANAMI_STRATEGY
    )
    apps_html = "".join(
        f"<div class='h-app'><span class='h-app-name'>&gt; {n}</span><span class='h-app-desc'>{d}</span></div>\n"
        for n, d in ESSENTIAL_APPS
    )
    eval_rows = ""
    for c, s, cm in eval_data():
        sc = "five" if "★★★★★" in s else ("four" if "★★★★☆" in s else "three")
        eval_rows += f"<tr><td class='hl'>{c}</td><td class='score-h {sc}'>{s}</td><td>{cm}</td></tr>\n"

    # 도시별 섹션
    city_sections = ""
    for ck in CITY_ORDER:
        cd = CITY_DATA[ck]
        yt = cd["youtube_dialect"]
        yt_url = f"https://youtu.be/{yt['id']}"

        tt_rows = "".join(
            f"<tr><td class='time-h'>[{t}]</td><td>{a}</td><td class='tip-h'>{tip}</td></tr>\n"
            for t, a, tip in cd["timetable"]
        )
        cs_rows = "".join(
            f"<tr><td class='sit-h'>{s}</td><td class='jp-h'>{l}</td><td class='note-h'>{n}</td></tr>\n"
            for s, l, n in cd["conversation_script"]
        )
        spots_li = "".join(
            f"<li><span class='sn-h'>{sn}</span> <span class='sr-h'>{sr}</span> — {sd}</li>\n"
            for sn, sr, sd in cd["spots"]
        )
        daytime_li = "".join(
            f"<li><span class='hl'>{dn}</span> : {dd}</li>\n"
            for dn, dd in cd["daytime"]
        )
        d_name, d_order, d_brand = cd["local_drink"]
        s_spot, s_time, s_tip = cd["sakura"]

        city_sections += f"""
<section class="h-city" id="{ck}">
  <div class="h-city-head">
    <div class="h-corner tl"></div><div class="h-corner tr"></div>
    <h2>// {cd['flag']} {cd['name_ko'].upper()} ({cd['name_jp']}) <span class="h-region">[ {cd['region']} ]</span></h2>
    <p class="h-tagline">&gt;&gt; {cd['tagline']}</p>
  </div>

  <div class="h-city-grid">
    <div class="h-col-main">

      <div class="h-block">
        <div class="h-block-title">[ ✈ FLIGHT INFO ]</div>
        <p class="h-p">{cd['flight']}</p>
        <p class="h-sub">&gt; {cd['flight_note']}</p>
        <p class="h-sub">&gt; ACCESS: {cd['access']}</p>
      </div>

      <div class="h-block yt-h-block">
        <div class="h-block-title">[ 📺 DIALECT TRAINING ]</div>
        <div class="h-yt-wrap">
          <a href="{yt_url}" target="_blank" rel="noopener">
            <img
              src="https://img.youtube.com/vi/{yt['id']}/hqdefault.jpg"
              alt="{yt['title']}"
              onerror="this.src='https://img.youtube.com/vi/{yt['id']}/mqdefault.jpg'"
            >
            <div class="h-play-overlay">
              <span class="h-play-btn">▶ PLAY</span>
              <span class="h-play-sub">유튜브에서 시청</span>
            </div>
          </a>
        </div>
        <p class="h-yt-title">&gt; <a href="{yt_url}" target="_blank">{yt['title']}</a></p>
        <p class="h-sub">CH: {yt['channel']}</p>
        <p class="h-sub">&gt;&gt; {yt['note']}</p>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 🍻 APPROACH STRATEGY ]</div>
        <p class="h-p"><span class="h-label">ZONE :</span> {cd['district']}</p>
        <p class="h-sub">{cd['district_desc']}</p>
        <p class="h-p"><span class="h-label">SCORE:</span> <span class="h-score">{cd['nanpa_score']}</span></p>
        <p class="h-sub">&gt; {cd['nanpa_reason']}</p>
        <div class="h-dialect">{cd['nanpa_dialect']}</div>
        <div class="h-strat-box">
          <span class="h-strat-label">// PLAN</span>
          <p>{cd['nanpa_strategy']}</p>
        </div>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ ⏰ NIGHT TIMETABLE ]</div>
        <table class="h-table">
          <thead><tr><th>TIME</th><th>ACTIVITY</th><th>TIP</th></tr></thead>
          <tbody>{tt_rows}</tbody>
        </table>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 💬 DIALOGUE SCRIPT ]</div>
        <table class="h-table">
          <thead><tr><th>STATUS</th><th>LINE (JP)</th><th>NOTE</th></tr></thead>
          <tbody>{cs_rows}</tbody>
        </table>
      </div>

    </div>

    <div class="h-col-side">

      <div class="h-block">
        <div class="h-block-title">[ 🍶 LOCAL DRINK ]</div>
        <p class="h-drink-name">&gt; {d_name}</p>
        <p class="h-order jp-h">{d_order}</p>
        <p class="h-sub">REC: {d_brand}</p>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 🌸 SAKURA POINT ]</div>
        <p class="hl">{s_spot}</p>
        <p class="h-sub">BLOOM: {s_time}</p>
        <p class="h-sub">&gt; {s_tip}</p>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ ☀ DAYTIME ]</div>
        <ul class="h-list">{daytime_li}</ul>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 🍺 IZAKAYA LIST ]</div>
        <ul class="h-list h-spots">{spots_li}</ul>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 🍽 LOCAL FOOD ]</div>
        <p class="h-food-name">{cd['food_name']}</p>
        <p class="h-sub">{cd['food_desc']}</p>
      </div>

      <div class="h-block">
        <div class="h-block-title">[ 🏨 BUDGET ]</div>
        <p class="h-sub">{cd.get('accommodation_detail', cd['accommodation'])}</p>
        <p class="h-budget">&gt; 2인 총: {cd['budget_2pax']}</p>
        <p class="h-budget">&gt; 1인 1일: {cd['budget_1p_day']}</p>
      </div>

    </div>
  </div>
  <div class="h-corner bl"></div><div class="h-corner br"></div>
</section>"""

    html = f"""<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<title>JAPAN NL GUIDE v3 // HOBIS EDITION</title>
<style>
/* ── HOBIS 테마 (스타크래프트 테란 감성) ── */
:root{{
  --bg:       #0d0f13;
  --panel:    #111418;
  --panel2:   #0a0d10;
  --cyan:     #00d4e8;
  --green:    #3dba5c;
  --green-l:  #00ff41;
  --orange:   #ff9500;
  --red:      #ff3838;
  --pink:     #ff6bcd;
  --grey:     #4a5568;
  --grey-l:   #8a95a8;
  --white:    #e2e8f0;
  --border:   rgba(0,212,232,.18);
  --border-g: rgba(61,186,92,.25);
  --glow-c:   0 0 8px rgba(0,212,232,.5);
  --glow-g:   0 0 8px rgba(61,186,92,.5);
}}
*{{box-sizing:border-box;margin:0;padding:0;}}
html{{scroll-behavior:smooth;}}
body{{
  font-family:'Courier New',Courier,monospace;
  background:var(--bg);color:var(--white);font-size:13px;line-height:1.6;
  background-image:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,0,0,.15) 2px,rgba(0,0,0,.15) 4px);
}}

/* ── 헤더 ── */
.h-header{{
  background:var(--panel2);
  border-bottom:2px solid var(--cyan);
  padding:18px 28px;
  position:sticky;top:0;z-index:200;
}}
.h-header h1{{
  font-size:20px;color:var(--cyan);
  text-shadow:var(--glow-c);
  letter-spacing:2px;text-transform:uppercase;
}}
.h-header .h-sub-title{{font-size:11px;color:var(--grey-l);margin-top:4px;letter-spacing:1px;}}
.h-header .h-meta{{font-size:10px;color:var(--grey);margin-top:3px;}}

/* ── 레이아웃 ── */
.h-layout{{display:flex;min-height:100vh;}}

/* ── 사이드바 ── */
.h-sidebar{{
  width:185px;min-width:185px;
  background:var(--panel2);
  border-right:1px solid var(--border);
  position:sticky;top:0;height:100vh;
  overflow-y:auto;padding:14px 0;
}}
.h-sidebar .sb-title{{
  font-size:9px;letter-spacing:2px;text-transform:uppercase;
  color:var(--grey);padding:6px 14px;border-bottom:1px dashed var(--border);
  margin-bottom:6px;
}}
.h-sidebar ul{{list-style:none;}}
.h-sidebar li a{{
  display:block;padding:6px 14px;color:var(--grey-l);
  text-decoration:none;font-size:11px;
  border-left:2px solid transparent;
  transition:all .15s;letter-spacing:.5px;
}}
.h-sidebar li a:hover{{
  background:rgba(0,212,232,.08);
  border-left-color:var(--cyan);
  color:var(--cyan);text-shadow:var(--glow-c);
}}

/* ── 메인 ── */
.h-main{{flex:1;padding:20px 24px;max-width:1100px;}}

/* ── 일반 섹션 카드 ── */
.h-section{{
  background:var(--panel);
  border:1px solid var(--border);
  border-radius:4px;
  padding:22px;margin-bottom:20px;
  position:relative;
}}
.h-section::before,.h-section::after,
.h-section>.h-tl,.h-section>.h-tr{{
  content:'';position:absolute;width:10px;height:10px;
}}
.h-section-title{{
  font-size:14px;color:var(--cyan);
  text-transform:uppercase;letter-spacing:2px;
  margin-bottom:14px;padding-bottom:8px;
  border-bottom:1px dashed var(--border);
  text-shadow:var(--glow-c);
}}
.h-section h3{{
  font-size:11px;color:var(--green);
  text-transform:uppercase;letter-spacing:1px;
  margin:14px 0 8px;
}}

/* ── 도시 섹션 ── */
.h-city{{
  background:var(--panel);
  border:1px solid var(--border-g);
  border-radius:4px;
  margin-bottom:28px;
  overflow:hidden;
  position:relative;
}}
.h-city-head{{
  background:linear-gradient(90deg,#0a1a0f 0%,#0d1f18 100%);
  border-bottom:1px solid var(--border-g);
  padding:18px 22px;
  position:relative;
}}
.h-city-head h2{{
  font-size:17px;color:var(--green-l);
  text-shadow:var(--glow-g);
  letter-spacing:1.5px;margin-bottom:4px;
}}
.h-region{{font-size:12px;color:var(--cyan);}}
.h-tagline{{font-size:11px;color:var(--grey-l);letter-spacing:.5px;}}

/* ── 코너 장식 ── */
.h-corner{{position:absolute;width:10px;height:10px;}}
.h-corner.tl{{top:0;left:0;border-top:2px solid var(--green-l);border-left:2px solid var(--green-l);}}
.h-corner.tr{{top:0;right:0;border-top:2px solid var(--green-l);border-right:2px solid var(--green-l);}}
.h-corner.bl{{bottom:0;left:0;border-bottom:2px solid var(--border-g);border-left:2px solid var(--border-g);}}
.h-corner.br{{bottom:0;right:0;border-bottom:2px solid var(--border-g);border-right:2px solid var(--border-g);}}

/* ── 도시 그리드 ── */
.h-city-grid{{display:grid;grid-template-columns:2fr 1fr;}}
.h-col-main{{padding:16px;border-right:1px solid var(--border);}}
.h-col-side{{padding:16px;background:#0a0d10;}}

/* ── 블록 ── */
.h-block{{margin-bottom:16px;padding-bottom:14px;border-bottom:1px dashed rgba(0,212,232,.1);}}
.h-block:last-child{{border-bottom:none;margin-bottom:0;}}
.h-block-title{{
  font-size:10px;color:var(--cyan);
  text-transform:uppercase;letter-spacing:2px;
  margin-bottom:9px;
  text-shadow:var(--glow-c);
}}
.h-p{{font-size:12px;margin-bottom:3px;}}
.h-sub{{font-size:10px;color:var(--grey-l);margin-bottom:2px;}}
.h-label{{color:var(--grey);font-size:10px;}}
.hl{{color:var(--green);}}
.h-score{{color:var(--orange);font-size:15px;letter-spacing:2px;}}
.h-dialect{{
  font-size:11px;color:var(--green-l);
  border:1px solid var(--border-g);
  padding:4px 10px;display:inline-block;
  border-radius:2px;margin:6px 0;
  text-shadow:var(--glow-g);
}}
.h-strat-box{{
  border-left:3px solid var(--green);
  padding:8px 12px;margin-top:9px;
  background:rgba(61,186,92,.05);
}}
.h-strat-label{{font-size:10px;color:var(--green);display:block;margin-bottom:3px;letter-spacing:1px;}}

/* ── YouTube 썸네일 (HOBIS) ── */
.yt-h-block{{background:#050810;border:1px solid rgba(0,212,232,.2);border-radius:4px;padding:14px;}}
.h-yt-wrap{{position:relative;margin:9px 0;border-radius:3px;overflow:hidden;}}
.h-yt-wrap img{{width:100%;display:block;filter:brightness(.85) saturate(.9);}}
.h-play-overlay{{
  position:absolute;top:0;left:0;width:100%;height:100%;
  background:rgba(0,13,20,.55);
  display:flex;flex-direction:column;align-items:center;justify-content:center;
  opacity:0;transition:.2s;
}}
.h-yt-wrap:hover .h-play-overlay{{opacity:1;}}
.h-play-btn{{
  font-size:22px;color:var(--green-l);
  text-shadow:var(--glow-g);letter-spacing:3px;
}}
.h-play-sub{{font-size:10px;color:var(--grey-l);margin-top:4px;}}
.h-yt-title{{font-size:11px;color:var(--cyan);margin-top:4px;}}
.h-yt-title a{{color:var(--cyan);text-decoration:none;}}
.h-yt-title a:hover{{text-shadow:var(--glow-c);}}

/* ── 테이블 ── */
.h-table{{width:100%;border-collapse:collapse;font-size:10px;margin-top:6px;}}
.h-table th{{
  background:#050810;color:var(--cyan);
  padding:5px 8px;text-align:left;
  font-size:9px;letter-spacing:1px;
  text-transform:uppercase;border-bottom:1px solid var(--border);
}}
.h-table td{{
  padding:5px 8px;border-bottom:1px solid rgba(0,212,232,.07);
  vertical-align:top;
}}
.h-table tr:hover td{{background:rgba(0,212,232,.04);}}
.time-h{{color:var(--orange);font-size:10px;white-space:nowrap;}}
.tip-h{{color:var(--grey-l);font-size:9px;}}
.sit-h{{color:var(--grey-l);font-size:10px;}}
.jp-h{{color:var(--green);font-family:serif;}}
.note-h{{font-size:9px;color:var(--grey-l);}}

/* ── 리스트 ── */
.h-list{{list-style:none;padding:0;}}
.h-list li{{
  font-size:11px;padding:4px 0;
  border-bottom:1px dashed rgba(0,212,232,.08);
  color:var(--grey-l);
}}
.h-list li:last-child{{border-bottom:none;}}
.sn-h{{color:var(--green);font-weight:700;}}
.sr-h{{color:var(--orange);font-size:10px;}}

/* ── 기타 ── */
.h-drink-name{{color:var(--cyan);font-size:13px;margin-bottom:4px;}}
.h-order{{color:var(--green-l);font-family:serif;}}
.h-food-name{{color:var(--orange);font-size:13px;margin-bottom:5px;}}
.h-budget{{color:var(--green);font-size:11px;margin-bottom:2px;}}
.h-card{{
  background:rgba(255,149,0,.07);border-left:3px solid var(--orange);
  padding:10px 13px;margin-bottom:8px;border-radius:0 4px 4px 0;
}}
.h-card.sakura-h{{background:rgba(255,107,205,.07);border-left-color:var(--pink);}}
.h-card-title{{font-size:11px;color:var(--orange);margin-bottom:3px;text-transform:uppercase;letter-spacing:.5px;}}
.h-card.sakura-h .h-card-title{{color:var(--pink);}}
.h-card p{{font-size:10px;color:var(--grey-l);}}
.h-app{{
  display:flex;align-items:flex-start;gap:8px;
  padding:6px 10px;margin-bottom:5px;
  background:rgba(0,212,232,.05);border-radius:3px;
  border-left:2px solid var(--border);
}}
.h-app-name{{font-size:11px;color:var(--cyan);min-width:200px;}}
.h-app-desc{{font-size:10px;color:var(--grey-l);}}

/* 공통 테이블 */
table.h-common{{width:100%;border-collapse:collapse;font-size:11px;margin:9px 0;}}
table.h-common th{{
  background:#050810;color:var(--cyan);padding:7px 10px;
  text-align:left;font-size:10px;letter-spacing:1px;text-transform:uppercase;
  border-bottom:1px solid var(--border);
}}
table.h-common td{{padding:6px 10px;border-bottom:1px solid rgba(0,212,232,.08);}}
table.h-common tr:hover td{{background:rgba(0,212,232,.04);}}

/* 평가 점수 색상 */
.score-h.five{{color:var(--green-l);text-shadow:var(--glow-g);}}
.score-h.four{{color:var(--cyan);}}
.score-h.three{{color:var(--grey-l);}}

/* formula */
.h-formula-box{{
  background:linear-gradient(90deg,#0a0a1e 0%,#0a1a14 100%);
  border:1px solid var(--border);border-radius:4px;
  padding:16px 20px;margin:12px 0;
}}
.h-formula{{font-size:12px;color:var(--green-l);text-shadow:var(--glow-g);letter-spacing:.5px;}}

/* conclusion */
.h-conclusion{{
  border:1px solid var(--border-g);border-radius:4px;
  padding:16px 20px;margin:12px 0;
  background:rgba(61,186,92,.05);
}}
.h-conclusion li{{font-size:11px;color:var(--grey-l);margin-bottom:6px;}}
.h-conclusion li b{{color:var(--green);}}

@media(max-width:900px){{
  .h-city-grid{{grid-template-columns:1fr;}}
  .h-col-main{{border-right:none;border-bottom:1px dashed var(--border);}}
  .h-sidebar{{display:none;}}
}}
@media print{{
  body{{background:#fff;color:#000;background-image:none;}}
  .h-sidebar,.h-play-overlay{{display:none;}}
  .h-header{{position:static;}}
}}
</style>
</head>
<body>
<header class="h-header">
  <h1>// JAPAN NL GUIDE v3 — HOBIS EDITION</h1>
  <div class="h-sub-title">&gt; ICN 직항 15개 소도시 | 이자카야·스낵바 공략 | 방언 접근 전략 | 목적달성 플랜</div>
  <div class="h-meta">TARGET: 2026.04 첫째 주 4박5일 | CREW: 일본어 능숙 한국 남성 2인</div>
</header>

<div class="h-layout">
  <nav class="h-sidebar">
    <div class="sb-title">// NAVIGATION</div>
    <ul>
      <li><a href="#strategy">[ STRATEGY ]</a></li>
      <li><a href="#tactics">[ TACTICS ]</a></li>
      <li><a href="#scam">[ SCAM DEF ]</a></li>
      <li><a href="#hanami">[ HANAMI ]</a></li>
      <li><a href="#cost">[ BUDGET ]</a></li>
      <li><a href="#apps">[ APPS ]</a></li>
      <li><a href="#cities">--- CITIES ---</a></li>
      {nav_items}
      <li><a href="#eval">[ EVAL ]</a></li>
    </ul>
  </nav>

  <main class="h-main">

    <section class="h-section" id="strategy">
      <div class="h-section-title">// 01 — STRATEGY OVERVIEW</div>
      <div class="h-formula-box">
        <p class="h-formula">FORMULA &gt; 방언 한 마디 → 관심 유도 → 합석 → 대화 심화 → LINE 교환 → 다음 자리 제안</p>
      </div>
      <h3>[ EXECUTION SEQUENCE ]</h3>
      <ol style="padding-left:18px;line-height:2.2;font-size:11px;color:var(--grey-l)">
        <li><span class="hl">T-14:</span> 방언 YouTube 시청. 핵심 표현 3개씩 암기</li>
        <li><span class="hl">T-7:</span> 도시 섹션 정독. 타임테이블·대화 스크립트 숙지</li>
        <li><span class="hl">D-DAY:</span> 타임테이블 따라 이자카야 진입. 방언 첫 마디 준비</li>
        <li><span class="hl">ON-SITE:</span> 대화 스크립트 참고. 자연스럽게 단계별 진행</li>
        <li><span class="hl">POST:</span> LINE 교환 후 귀국 후에도 연락 유지</li>
      </ol>
      <h3>[ WARNINGS ]</h3>
      <ul style="padding-left:18px;font-size:10px;line-height:2.2;color:var(--grey-l)">
        <li>&gt; 항공 가격은 2026.03 기준 — 실제 예약 시 항공사 공식 사이트 재확인</li>
        <li>&gt; 스낵바 입장료·세트는 가게마다 편차 큼 — 입장 전 반드시 직접 확인</li>
        <li>&gt; 4월 첫째 주는 골든위크 직전 — 호텔 가격 상승 주의</li>
        <li>&gt; 벚꽃 개화 시기 매년 변동 — 여행 직전 sakura.info 실시간 확인</li>
      </ul>
    </section>

    <section class="h-section" id="tactics">
      <div class="h-section-title">// 02 — APPROACH STRATEGY</div>
      <h3>[ BY LOCATION ]</h3>
      <table class="h-common">
        <thead><tr><th>장소</th><th>접근 전략</th></tr></thead>
        <tbody>{strategy_rows}</tbody>
      </table>
      <h3>[ BY TIME ]</h3>
      <table class="h-common">
        <thead><tr><th>시간대</th><th>전략</th></tr></thead>
        <tbody>
          <tr><td class="time-h">[17:00~19:00]</td><td>밥집·야타이 1차. 퇴근 후 첫 술자리. 자연스러운 첫 접촉 최적.</td></tr>
          <tr><td class="time-h">[19:00~21:00]</td><td>이자카야 메인 시간대. 분위기 무르익음. 합석·대화 성공률 최고.</td></tr>
          <tr><td class="time-h">[21:00~23:00]</td><td>스낵바·바 2차. 경계심 낮아진 상태 — 대화 진입 용이.</td></tr>
          <tr><td class="time-h">[23:00~02:00]</td><td>클럽·심야 바. LINE 교환 또는 3차 제안 마지막 기회.</td></tr>
        </tbody>
      </table>
      <h3>[ COMMON DIALOGUE ]</h3>
      <table class="h-common">
        <thead><tr><th>상황</th><th>일본어</th><th>해설</th></tr></thead>
        <tbody>{tips_rows}</tbody>
      </table>
    </section>

    <section class="h-section" id="scam">
      <div class="h-section-title">// 03 — SCAM DEFENSE</div>
      {scam_html}
    </section>

    <section class="h-section" id="hanami">
      <div class="h-section-title">// 04 — HANAMI STRATEGY</div>
      {hanami_html}
    </section>

    <section class="h-section" id="cost">
      <div class="h-section-title">// 05 — BUDGET GUIDE</div>
      <table class="h-common">
        <thead><tr><th>항목</th><th>비용</th><th>설명</th></tr></thead>
        <tbody>{cost_rows}</tbody>
      </table>
      <div style="border:1px solid var(--border-g);border-radius:3px;padding:10px 14px;margin-top:12px;font-size:11px;color:var(--green)">
        &gt; 2인 4박 5일 총: ¥300,000~600,000 (1인 ¥150,000~300,000)<br>
        <span style="font-size:10px;color:var(--grey-l)">&gt;&gt; 항공권 40~50% 차지 → 조기 예약이 핵심 절약 포인트</span>
      </div>
    </section>

    <section class="h-section" id="apps">
      <div class="h-section-title">// 06 — REQUIRED APPS</div>
      {apps_html}
    </section>

    <div id="cities" style="margin:28px 0 10px;border-bottom:2px solid var(--border-g);padding-bottom:10px">
      <p style="font-size:16px;color:var(--green-l);text-shadow:var(--glow-g);letter-spacing:2px">// 07 — CITY PLANS [15 CITIES]</p>
      <p style="font-size:10px;color:var(--grey);margin-top:5px;letter-spacing:.5px">
        PER CITY: FLIGHT &gt; DIALECT TRAINING &gt; APPROACH STRATEGY &gt; NIGHT TIMETABLE &gt; LOCAL DRINK &gt; SAKURA &gt; DAYTIME &gt; SPOTS &gt; DIALOGUE &gt; BUDGET
      </p>
    </div>

    {city_sections}

    <section class="h-section" id="eval">
      <div class="h-section-title">// 08 — MISSION EVALUATION</div>
      <table class="h-common">
        <thead><tr><th>도시</th><th>적합도</th><th>평가</th></tr></thead>
        <tbody>{eval_rows}</tbody>
      </table>
      <h3>[ FINAL LOG ]</h3>
      <div class="h-conclusion">
        <ul style="padding-left:16px">
          {''.join(f'<li>{l}</li>' for l in CONCLUSION)}
        </ul>
      </div>
      <p style="font-size:10px;color:var(--grey);margin-top:16px;text-align:center;letter-spacing:1px">
        // 일본 문화와 이자카야 예절을 존중하는 범위 내에서 활용하시기 바랍니다. //
      </p>
    </section>

  </main>
</div>
</body>
</html>"""

    out = os.path.join(BASE_DIR, "20260401_일본나이트라이프가이드_v3_HOBIS.html")
    with open(out, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"✅ HOBIS HTML 저장: {out}  ({os.path.getsize(out)//1024}KB)")
    return out


# ════════════════════════════════════════════════════════════════
#  메인
# ════════════════════════════════════════════════════════════════
if __name__ == "__main__":
    print("=" * 55)
    print("테마 HTML 생성 시작")
    print("=" * 55)
    p1 = build_html_v3()
    p2 = build_html_hobis()
    print("\n완료!")
    print(f"  표준: {p1}")
    print(f"  HOBIS: {p2}")
