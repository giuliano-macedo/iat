from urllib.request import urlopen
import zipfile
import io
from tqdm import tqdm
def download_file(url):
	def download(res):
		while True:
			chunk = res.read(1000)
			if not chunk:
				return
			yield chunk
	ans=bytearray()
	res = urlopen(url)
	total=int(res.info().get('content-length', 0))
	t=tqdm(total=total,unit='B', unit_scale=True)
	for chunk in download(res):
		t.update(len(chunk))
		ans+=chunk
	t.close()
	return ans
def download_and_extract_zip(url,path):
	f=io.BytesIO(download_file(url))
	my_zip=zipfile.ZipFile(f)
	my_zip.extractall(path)
