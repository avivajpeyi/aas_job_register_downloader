from .html_parser import download_page


def get_job_description(job_url) -> str:
    page = download_page(job_url)
    description_html = page.find_all("p")
    description = [line.get_text() for line in description_html]
    return "\n".join(description)
