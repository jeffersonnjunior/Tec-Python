from .bus_routes import BusRoutesScraper

def run_scraper(start_text:str, destination_text:str) -> list[str]:
    scraper = BusRoutesScraper(start_text, destination_text)
    return scraper.run()

__all__ = ['run_scraper']
