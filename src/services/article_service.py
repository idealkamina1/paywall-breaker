class ArticleService:
    def __init__(self, extractor, bypasser):
        self.extractor = extractor
        self.bypasser = bypasser

    def fetch_article(self, url):
        """
        Fetches the article from the given URL. 
        It first attempts to bypass the paywall and then extracts the content.
        """
        if self.bypasser.bypass_paywall(url):
            content = self.extractor.extract_text(url)
            images = self.extractor.extract_images(url)
            return {
                "content": content,
                "images": images
            }
        else:
            raise Exception("Unable to bypass paywall for the given URL.")

    def save_article(self, article_data):
        """
        Saves the article data to a database or a file.
        This is a placeholder for the actual implementation.
        """
        # Implementation for saving the article data goes here
        pass