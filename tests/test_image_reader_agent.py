from agents import ImageReaderAgent

def test_image_reader_agent():
    agent = ImageReaderAgent(name="Image Reader")
    image_path = "sample_image.png"  # Replace with the path to your image file
    result = agent.perform_task(image_path, None)  # LLM is not needed for this task
    print(result)

if __name__ == "__main__":
    test_image_reader_agent()