from autogen import AssistantAgent, UserProxyAgent


class CustomAssistantAgent(AssistantAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_behavior = kwargs.get("custom_behavior", {})

    def process_message(self, message):
        # Add custom processing logic here
        processed_message = super().process_message(message)
        if self.custom_behavior.get("add_signature", False):
            processed_message += f"\n\nBest regards,\n{self.name}"
        return processed_message


class CustomUserProxyAgent(UserProxyAgent):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.custom_behavior = kwargs.get("custom_behavior", {})

    def generate_response(self, message):
        # Add custom response generation logic here
        response = super().generate_response(message)
        if self.custom_behavior.get("add_timestamp", False):
            from datetime import datetime

            response += (
                f"\n\nGenerated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            )
        return response
