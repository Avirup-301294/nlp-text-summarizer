from src.textSummarizer.config.configuration import ConfigurationManager
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch


class PredictionPipeline:
    def __init__(self):
        self.config = ConfigurationManager().get_model_evaluation_config()
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def predict(self, text):
        tokenizer = AutoTokenizer.from_pretrained(self.config.tokenizer_path)
        model = AutoModelForSeq2SeqLM.from_pretrained(self.config.model_path)
        model = model.to(self.device)
        model.eval()
        
        gen_kwargs = {
            "length_penalty": 0.8,
            "num_beams": 8,
            "max_length": 128,
            "min_length": 30,
            "early_stopping": True,
            "no_repeat_ngram_size": 3,
            "do_sample": False
        }

        print("Dialogue:")
        print(text)

        # Tokenize the input text
        inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
        inputs = {k: v.to(self.device) for k, v in inputs.items()}
        
        # Generate summary
        with torch.no_grad():
            summary_ids = model.generate(
                inputs["input_ids"],
                attention_mask=inputs["attention_mask"],
                **gen_kwargs
            )
        
        # Decode the summary
        output = tokenizer.batch_decode(summary_ids, skip_special_tokens=True)[0]
        
        print("\nModel Summary:")
        print(output)

        return output
