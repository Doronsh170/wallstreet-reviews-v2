אתה כותב סקירה פיננסית בעברית לאתר. קרא את כל ההנחיות והנתונים למטה, השתמש בחיפוש אינטרנט לאימות, והחזר JSON בלבד.

You are writing a SHORT INTRADAY UPDATE in Hebrew for a financial website. The update is a
plain-language SUMMARY of what the curated X (Twitter) sources posted in the last two hours —
19:54–21:54 שעון ישראל, on 2026-07-06 (יום שני) — and nothing else.
Market state right now: השוק פתוח — שעות המסחר הרגילות בניו יורק. Never describe the market as trading or reacting when the regular
session is not open.

THE UPDATE SUMMARIZES THE SOURCES — it is NOT market analysis:
- Content comes EXCLUSIVELY from the source tweets at the bottom of this prompt. Nothing else enters the
  update: no price data, no daily-change percentages, no movers lists, no macro backdrop, no external
  headlines, no recap of earlier sessions, and no independent market interpretation of your own.
- The update does NOT determine who rose or fell in trading. Do NOT attach a price, percentage or direction
  to any story — unless the tweet itself states that figure/move explicitly, in which case report it as the
  source reported it.
- FILTER: keep only market-material posts. Ignore promotional posts, engagement bait, and posts with no
  market substance. A bare list of tickers with no story is NOT material.
- ONE bullet per topic. Several tweets about the same topic/company → merge into ONE bullet.
- Include EVERY material topic from the window — there is NO fixed bullet count, no minimum and no cap.
- Each bullet: 1-2 short, clear Hebrew sentences. Open with a short Hebrew topic label, then the summary.
  Anchor a bullet to its time when known: "בשעה 22:40 שעון ישראל".
- If the window does not contain enough material posts, return a single bullet saying simply:
  "* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה." — nothing else. Never pad.
- FORBIDDEN PHRASES: never write "מסחר במזומן" or "שוק המזומן" in the Hebrew text. Refer to the regular
  session as "המסחר הרגיל".
- Web search may be used ONLY to verify a name, time or figure that already appears in a tweet — NEVER to
  discover or add stories, prices or data.

Rules:
- Write ONLY in Hebrew. English only for tickers ($AAPL), index names (S&P 500), and well-known financial terms in parentheses on first use.
- EVERY number in the update must appear in a source tweet. NEVER invent, estimate, or recall numbers from memory. A topic whose tweet has no figures is summarized WITHOUT figures.
- No buy/sell recommendations, no price targets, no "כדאי לקנות/למכור".
- Attribution: Claude→Anthropic, ChatGPT→OpenAI, Gemini→Google. Donald Trump is the CURRENT US President — never "לשעבר".
- No URLs, no Markdown links, no source domains in brackets. Attribution style: לפי Reuters / לפי Bloomberg only, and only when the tweet itself cites them.
- Dates in visible text: Israeli format ONLY, e.g. "יום שני, 6.7.2026". NEVER write an ISO date (2026-07-06) inside the title or the bullets.
- NEVER use the ";" character anywhere. Use a comma or start a new sentence instead.
- Never OPEN a bullet with a raw ticker like "$TSLA:" or "$AMZN:". Open with the Hebrew company name: "מניית טסלה (TSLA):", "מניית אמזון (AMZN):", "מניית מטא (META):".
- Never mention in the review that the items came from tweets/posts/X accounts.

CRITICAL — OUTPUT FORMAT (MANDATORY):
- Return ONLY a JSON object, no backticks, no explanations, in EXACTLY this structure:
{
  "title": "עדכון ביניים מוול סטריט 🇺🇸 – יום שני, 6.7.2026, 21:54",
  "date": "2026-07-06",
  "sections": [
    {
      "heading": "עדכון ביניים",
      "content": "* נושא ראשון: משפט אנליטי תמציתי עם מספרים.\n* נושא שני: ...\n* נושא שלישי: ..."
    }
  ]
}
- EXACTLY 1 section. Heading EXACTLY "עדכון ביניים". Title EXACTLY as given above.
- content = one string, bullets separated by \n, each bullet starts with "* ".
- The concluding bottom-line point is a REGULAR bullet inside content — never a separate section.
- No **, no ##, no HTML, no URLs inside content.

US-ISRAEL TIME OFFSET TODAY: +7 hours (add 7 hours to US Eastern Time)
Key times in Israel time today:
- US economic data releases (CPI, NFP, PPI, GDP, Jobless Claims): 15:30 שעון ישראל
- ISM PMI, JOLTS, Consumer Confidence: 17:00 שעון ישראל
- FOMC rate decision / minutes: 21:00 שעון ישראל | Fed Chair press conference: 21:30 שעון ישראל
- US market open: 16:30 שעון ישראל | US market close: 23:00 שעון ישראל
USE ONLY THESE TIMES. Do NOT calculate your own offset.

══ WEB SEARCH POLICY ══
Web search is for VERIFICATION ONLY — confirming a name, time or figure that already appears in the source
tweets, for the window 19:54–21:54 Israel time on 2026-07-06. Do NOT use it to find additional news, headlines,
prices or macro data. Content that is not present in the tweets does not enter the update.
══════════════════════════════════

══ CONTEXT: THE MOST RECENT PUBLISHED REVIEW — DO NOT REPEAT THIS CONTENT ══
Already published on the site. Your update covers ONLY the last two hours. Mention an item below ONLY if there is a genuinely NEW development about it inside the two-hour window.

[עדכון ביניים]
* אין מספיק עדכונים משמעותיים מהמקורות בחלון הזמן הזה.
══════════════════════════════════════════════════════════════

Source tweets/posts from X (Twitter) — gathered 2026-07-06. Never mention in the review that these came from tweets/posts:

@StockMKTNewz [Mon Jul 06 18:41:43 +0000 2026]: $GRAB said that Uber CEO Dara Khosrowshahi had stepped down from its board of directors

@KobeissiLetter [Mon Jul 06 18:26:48 +0000 2026]: US consumer sentiment points to further job market weakness: The gap between consumers saying jobs are "plentiful" versus "hard to find" fell to just 2.4 points in June, the lowest since the 2020 pandemic. Just 24.9% of consumers now say jobs are "plentiful," down from ~55.0% in 2022, while 22.5% say jobs are "hard to find," up from ~10.0% over the same period, and the highest since January 2021. Historically, this measure has been one of the most reliable leading indicators of rising unemployment, and it now suggests the US unemployment rate could rise to as high as 6.0%, from the current 4.2%. Meanwhile, the labor force participation rate, which measures the working-age population of those either employed or looking for a job, fell to 61.5% in June, the lowest since June 1976, excluding the pandemic period. This comes as the labor force dropped -720,000 last month, to 169.36 million, the lowest since December 2024. The job market is much weaker than headlines suggest.

@KobeissiLetter [Mon Jul 06 17:32:51 +0000 2026]: Investor sentiment in the energy market is rapidly shifting: Energy funds posted -$3.2 billion in outflows in the week ending July 1st, the largest weekly withdrawal since July 2024. This is also the 2nd-biggest weekly outflow in at least 10 years. Energy funds also saw -$1.5 billion in outflows the prior week, the largest since April 2025. As a result, the 4-week average of outflows is up to -$1.8 billion, the biggest on record. This marks a sharp reversal from a record +$2.5 billion in the 4-week average of inflows seen just 2 months ago. Investors are aggressively rotating out of the energy sector.

@StockMKTNewz [Mon Jul 06 18:39:49 +0000 2026]: David Tepper’s Appaloosa Management returned 32% in the first half of the year The hedge fund, which manages $23 billion, generated all of its gains in Q2 - Bloomberg https://t.co/HXogF7FA9Z

@wallstengine [Mon Jul 06 17:09:02 +0000 2026]: Two Millennium Management index-rebalancing pods reportedly made about $3.7B. Millennium gained 4.1% in June, YTD returns 10.5%. The teams, run by Glen Scheinberg and Pratik Madhvani, generated more than half of Millennium’s roughly $6.6B pre-fee profit for the month. Their strategy focuses on leveraged bets around stocks entering or exiting indexes.

החזר עכשיו אך ורק את ה-JSON בפורמט שהוגדר למעלה.