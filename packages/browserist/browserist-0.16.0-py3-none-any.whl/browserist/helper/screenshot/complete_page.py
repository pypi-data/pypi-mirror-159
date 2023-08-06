from ...browser.scroll.check_if.is_end_of_page import check_if_scroll_is_end_of_page
from ...browser.scroll.get.position import get_scroll_position
from ...browser.scroll.page.down import scroll_page_down
from ...browser.scroll.page.to_top import scroll_to_top_of_page
from ...browser.scroll.to_position import scroll_to_position
from ...model.screenshot import ScreenshotTempDataHandler


def firefox(driver: object, destination_file_path: str) -> None:
    driver.get_full_page_screenshot_as_file(destination_file_path)  # type: ignore


def default(driver: object, destination_file_path: str, destination_dir: str, delay_seconds: float) -> None:
    def get_screenshot_of_visible_portion_and_scroll_down(driver: object, handler: ScreenshotTempDataHandler, delay_seconds: float) -> None:
        handler.save_screenshot(driver)
        handler.increment_iteration()
        scroll_page_down(driver, delay_seconds)

    # Save inital scroll position so we can return to it later.
    x_inital, y_initial = get_scroll_position(driver)

    # Prepare for iteration from the top of the page.
    scroll_to_top_of_page(driver, delay_seconds)
    handler = ScreenshotTempDataHandler(destination_dir=destination_dir, destination_file_path=destination_file_path)

    # Take screenshots of the visible portion until we reach the end of the page.
    get_screenshot_of_visible_portion_and_scroll_down(driver, handler, delay_seconds)
    while check_if_scroll_is_end_of_page(driver) is not True:
        get_screenshot_of_visible_portion_and_scroll_down(driver, handler, delay_seconds)

    # TODO: Consider refactoring to async methods so it runs faster:
    handler.merge_temp_files_into_final_screenshot()

    # Return to initial scroll position and tidy up temp files.
    scroll_to_position(driver, x_inital, y_initial, delay_seconds)
    handler.remove_temp_files()
