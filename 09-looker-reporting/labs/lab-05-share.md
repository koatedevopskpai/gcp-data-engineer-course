# Lab 09.5 — Share, Schedule & Embed

## Objectives
- Share the report, schedule email delivery, embed in a web page.

## 1. Share
1. Click **Share** (top-right).
2. Add emails with **Viewer** or **Can edit** rights.
3. Optionally **Manage access → Anyone with the link**.

## 2. Schedule email delivery
1. **File → Report settings → Schedule email delivery**.
2. Set frequency (daily/weekly), recipients, and email subject.

## 3. Embed in a website
```html
<iframe
  src="https://lookerstudio.google.com/embed/report/YOUR_REPORT_ID/page/1"
  width="100%" height="100%" frameborder="0" allowfullscreen>
</iframe>
```

## Exam notes
- Embedding requires the report to be shared appropriately (link sharing on).
- For **Looker**, embedding is via the Embed SDK and LookML models — different from Looker Studio iframes.
