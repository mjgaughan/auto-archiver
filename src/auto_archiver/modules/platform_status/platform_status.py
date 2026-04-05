from datetime import datetime
from auto_archiver.core import Metadata
from auto_archiver.version import __version__

class PlatformStatus:
	def __init__(
		self,
		metadata: Metadata,
		platform_name: str,
		url: str,
		content_type: str,
	) -> None:
		#platform status eval metadata
		self.id = f"{datetime.now().isoformat()}_{platform_name}_{content_type}"
		self.metadata: Metadata = metadata
		self.run_datetime: datetime = datetime.now()
		self.current_metadata = self.metadata.metadata
		self.aa_version: str = __version__
		#platform status eval specifics
		self.platform_name: str = platform_name
		self.trial_url: str = url
		self.content_type: str = content_type
		self.isContentAccessible: bool = False
		self.isContentArchived: bool = False

	def ContentAccessible(self, accessible: bool) -> None:
		self.isContentAccessible = accessible
	
	def ContentArchived(self, archived: bool) -> None:
		self.isContentArchived = archived
