import requests
import gzip
import io

def main():
    try:
        # Step 1: Download the .gz index file
        base_url = 'https://data.commoncrawl.org'
        gz_path = '/crawl-data/CC-MAIN-2022-05/wet.paths.gz'
        url = base_url + gz_path

        print(f"Downloading from: {url}")
        response = requests.get(url)
        response.raise_for_status()

        # Step 2: Read .gz content from memory
        with gzip.GzipFile(fileobj=io.BytesIO(response.content), mode='rb') as gz_file:
            content = gz_file.read().decode('utf-8')
            lines = content.splitlines()

            if not lines:
                raise Exception("No lines found in the gz file")

            # Step 3: Get first WET file URI
            first_uri = lines[0]
            print(f"First URI: {first_uri}")

            # Step 4: Convert S3 URI to HTTPS
            file_path = first_uri.replace('s3://commoncrawl/', '')
            domains = [
                'https://data.commoncrawl.org',
                'https://commoncrawl.s3.amazonaws.com',
                'https://cc-index.commoncrawl.org'
            ]

            success = False
            for domain in domains:
                try:
                    file_url = f"{domain}/{file_path}"
                    print(f"Trying to download from: {file_url}")

                    # Step 5: Stream download
                    with requests.get(file_url, stream=True) as r:
                        r.raise_for_status()
                        buffer = io.BytesIO()
                        for chunk in r.iter_content(chunk_size=8192):
                            if chunk:
                                buffer.write(chunk)
                        buffer.seek(0)

                        # Step 6: Read only first 10 lines
                        print("\n--- First 10 lines of content ---")
                        with gzip.GzipFile(fileobj=buffer, mode='rb') as gz_file:
                            for i, line in enumerate(gz_file):
                                if i >= 10:
                                    break
                                print(line.decode('utf-8').strip())
                        print("--- End of preview ---\n")

                        success = True
                        break
                except Exception as e:
                    print(f"Failed with domain {domain}: {str(e)}")

            if not success:
                raise Exception("Failed to download from all domains")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
