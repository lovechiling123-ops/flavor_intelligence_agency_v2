---
name: Flavor Intelligence Agency (美味中情局)
description: A personalized AI restaurant tracking tool built with single-file HTML, Tailwind CSS, and LocalStorage.
---

# 🕵️‍♂️ Flavor Intelligence Agency (美味中情局)

## 專案概述 (Project Overview)
「美味中情局 (FIA) aka 個人化 AI 美食情報戰情室」是一個專為美食情報員打造的單頁應用程式（SPA）。
旨在解決現代人面對大量社群推薦資訊（如 IG、Google Maps 短影音）時「缺乏系統性整理」以及「用餐時毫無靈感」的痛點。

這套工具會將碎片化的資訊結構化，變成自己的美食情報庫。目前為**單機純前端版本**，無需部署伺服器即可在本地瀏覽器直接執行。

## 系統架構與技術棧 (Architecture & Tech Stack)
1. **前端核心**：純 HTML5 + Vanilla JavaScript (ES Module)。
2. **UI 與樣式**：Tailwind CSS (CDN 掛載) + 客製化 CSS，主要字體使用 `Noto Sans TC` 與 `JetBrains Mono`。
3. **資料庫引擎**：瀏覽器 `localStorage` (Key: `cia_restaurants_db_flavor-bureau-default`)。
4. **主要功能模組**：
   - **情報決策引擎** (`decisionCanvas`)：利用 HTML5 Canvas 實作的動態卡片翻牌動畫（美味靈感發射器）。
   - **情報建檔** (`entryForm`)：快速輸入店家資訊並自動辨識台灣行政區。
   - **情報資料庫** (`restaurantList`)：可搜尋、排序、編輯的情報列表，並支援一鍵啟動 Google Maps 戰術導航。
   - **資料轉移中心** (`backupModal`)：支援匯出 `.json` 備份檔及暗號（Base64 序列化）兩種資料轉移模式。

## 開發與修改指南 (Developer Guidelines)
當 AI（或開發者）被要求修改此工具時，必須嚴格遵守以下守則：

### 1. 狀態與資料同步 (State & Syncing)
所有的資料修改（如：新增、刪除、復原）都必須針對全域變數 `restaurants` 陣列進行操作。操作完成後，必須呼叫全域函數 `SYNC_DATA()`，該函數會負責：
- 將最新資料序列化至 `localStorage`。
- 呼叫 `renderList()` 重新渲染情報資料庫。
- 呼叫 `initCards()` 刷新決策引擎的卡片內容。

### 2. UI/UX 視覺一致性 (UI/UX Consistency)
- 新增元件時，請繼續使用 `slate` (灰藍) 與 `orange/amber` (琥珀/亮橘) 作為主要色系。
- 卡片或視窗必須具備無斷點的強烈圓角特色 (`rounded-[2.5rem]` 或 `rounded-2xl`)。
- **絕對禁止**使用瀏覽器原生的 `alert()`。必須統一使用自製的 `window.showCIAAlert("你的訊息")` 或 `showToast("小提示")` 來與用戶互動。

### 3. 架構限制 (Limitations)
- 在使用者明確要求加入 Node.js 或是後端框架之前，**絕對不要**隨意將目前的單檔 (`index.html`) 架構破壞、或是引入需要編譯（Build）的工具（如 Webpack/Vite）。
- 保持其可以在任何電腦點擊 `index.html` 就能直接執行的特性。

### 4. 開發執行鐵則 (Strict Execution Rules)
每次進行開發或修改前，AI 必須嚴格遵守以下四項鐵則：
1. **跨平台相容**：製作與新增的所有功能與畫面，必須符合 PC、手機（iOS 系統、Android 系統）的響應式顯示體驗與操作可用性。
2. **事前確認制**：正式修改程式碼前，必須先列出即將更動/新增的功能清單、編纂好新版本號，並向局長（使用者）取得明確的「確認」後，才可以著手執行更改。
3. **精準局部修改**：每次執行製作時，只能限縮更動在「已討論好」的範圍內。嚴格禁止擅自更動無關的功能；如果因為系統相依性而必定要動到其他功能，必須「先」詢問局長。
4. **版本存檔/重構退路**：每一次的改動與製作前，必須進行存檔或備份（例如將舊版複製一份），以確保無論什麼時候出錯，都能隨時可以退版使用。
5. **完工回報格式 (Post-Release Report)**：每次改版完成後，必須向局長列出此格式：包含「標題（例如 V1.9 簡短標題）」、「改版內容 (1, 2, 3...)」與「簡易測試項目 (1, 2, 3...)」。

## 未來擴充路線 (Roadmap)
此工具規劃在未來導入：
- **AI 多模態情資提取**：這將會是下一個重點功能，支援輸入網址或截圖，自動利用 AI 解析並填入住址、特色與店名。
- **雲端資料庫切換**：未來可能重新掛載 Firebase 連線，將資料轉移至雲端。
