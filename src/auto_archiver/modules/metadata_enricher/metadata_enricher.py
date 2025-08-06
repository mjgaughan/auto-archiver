import subprocess
import traceback
from auto_archiver.utils.custom_logger import logger

from auto_archiver.core import Enricher
from auto_archiver.core import Metadata


class MetadataEnricher(Enricher):
    """
    Extracts metadata information from files using exiftool.
    """

    def enrich(self, to_enrich: Metadata, md_grocery_list=["gps", "datetimes", "author"]) -> None:
        logger.debug("Extracting EXIF metadata")

        for i, m in enumerate(to_enrich.media):
            if len(md := self.get_metadata(m.filename)):
                # TODO: feature flag has this currently turned off
                # specified_md = self.select_metadata(md_grocery_list, md)
                # to_enrich.media[i].set("metadata", specified_md)
                to_enrich.media[i].set("metadata", md)

    def get_metadata(self, filename: str) -> dict:
        try:
            # Run ExifTool command to extract metadata from the file
            cmd = ["exiftool", filename]
            result = subprocess.run(cmd, capture_output=True, text=True)
            # Process the output to extract individual metadata fields
            metadata = {}
            for line in result.stdout.splitlines():
                field, value = line.strip().split(":", 1)
                metadata[field.strip()] = value.strip()
            return metadata
        except FileNotFoundError as e:
            logger.error(f"ExifTool not found. Make sure ExifTool is installed and added to PATH. {e}")
        except Exception as e:
            logger.error(f"Error occurred: {e}: {traceback.format_exc()}")
        return {}

    def select_metadata(self, md_grocery_list, all_md):
        """
        coordinates the selection of metadata from the general exiftool output to the user-specified grocery list
        """
        specified_md = {}
        # below is a switch for the specified metadata, not sure this is the most elegant way to do this
        if "author" in md_grocery_list:
            # TODO: swap in logic for grabbing author
            specified_md["author"] = "author"
        elif "datetimes" in md_grocery_list:
            # TODO: swap in logic for grabbing datetimes
            specified_md["datetimes"] = "datetimes"
        elif "gps" in md_grocery_list:
            # TODO: swap in logic for grabbing lat/lon info
            specified_md["gps"] = "gps"
