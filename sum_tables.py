from playwright.sync_api import sync_playwright

def get_seed_sum(page, seed):
    url = f"https://sanand0.github.io/tdsdata/js_table/?seed={seed}"
    page.goto(url)
    page.wait_for_load_state("networkidle")

    total = 0
    tables = page.locator("table").all()

    for table in tables:
        cells = table.locator("td, th").all()
        for cell in cells:
            text = cell.text_content().strip()
            text = text.replace(",", "")
            if text.replace(".", "", 1).isdigit():
                total += float(text)

    return total

def main():
    grand_total = 0
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()

        for seed in range(2, 12):
            grand_total += get_seed_sum(page, seed)

        print("FINAL TOTAL:", grand_total)
        browser.close()

main()
