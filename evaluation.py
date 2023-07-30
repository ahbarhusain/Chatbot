import nltk
from nltk.translate.bleu_score import sentence_bleu

# Sample data for evaluation (synthetic data)
questions = [
    "What is the cost/fees of a PAN card?",
    "Can I take the delivery of Pan card at Indian address",
    "How long does it usually take to receive the PAN card after applying?",
    "What are the charges of linking Pan & Aadhaar"
]

reference_answers = [
    "The cost of applying for a new PAN card is Rs 2500 for E-PAN. If you want it to be couriered, it will cost Rs 1200 extra for physical delivery to your address. Kindly note that this cost is only for applying for a new PAN card and not for linking PAN with Aadhaar.",
    "Yes, you can take the delivery of your PAN card only at an Indian address mentioned in your Aadhaar card. While applying for a new PAN card or requesting corrections, you can provide your Indian address as the delivery address. Make sure to provide accurate and complete address details to ensure successful delivery.",
    "Once the payment is made, we will contact you and initiate the process. Pan card will be issued in 3 weeks after submitting the application. You can get an e-Pan Card in under 10 minutes, if you have an Aadhaar card.",
    "The charges for linking Pan & Aadhaar is INR 2000/-, including the penalty charges to be paid for the delay in linking Pan & Aadhaar. It is important to link your PAN and Aadhaar cards to avoid any legal complications in India."
]

generated_answers = [
    "e-PAN Card cost: INR 2500 - Physical PAN Card cost: Sources:[Document(page_content='### Cost of new PAN card\n\nThe PAN CARD Application through ABC costs Rs 2500 for E-PAN, and if you want it to be couriered, it will cost Rs 1200 extra for physical delivery to your address.\n\n- e-PAN Card cost: INR 2500\n- Physical PAN Card cost: INR 3700\n\n### Time required to issue PAN card\n\nIf you have Aadhaar card\n\nYou can get a Pan Card instantly\xa0**(in under 10 minutes), if you have an Aadhaar card. You can apply through ABC.', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'}), Document(page_content='### Charges for reprinting the PAN Card**\n\nThe charges for reprinting the PAN Card are INR 2500 for e-pan, and INR 3700 for physical pan card.\n\n---\n\n## Linking PAN with Aadhaar card\n\nABC can link your PAN card and Aadhaar card on your behalf. \n\n### Process to link PAN with Aadhaar\n\n- Go to ABC app\n- Navigate to Services > NRI PAN Card > Link PAN with Aadhaar\n- Request reissue the required PAN card and make the payment\n- Our team will reach out to you for the required documents', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'})]",
    "Yes, you can take the delivery of your PAN card only at an Indian address mentioned in your Sources:[Document(page_content='Yes, you can take the delivery of your PAN card only at an Indian address mentioned in your Aadhaar card. While applying for a new PAN card or requesting corrections, you can provide your Indian address as the delivery address. Make sure to provide accurate and complete address details to ensure successful delivery.', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'}), Document(page_content='Can I apply for a PAN card if I am a non-resident Indian (NRI)?\n\nYes, as an NRI, you can apply for a PAN card. The process for applying for a PAN card is the same for both residents and NRIs. However, if you are an OCI holder or a person of Indian origin who holds foreign citizenship, you will need to fill Form 49AA to apply for a PAN card.\n\nCan I take the delivery of Pan card at Indian address?', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'})]",
    "2-3 weeks Sources:[Document(page_content='Time required to complete the correction process for the PAN card: The duration to complete the correction process for your PAN card can vary, but it generally takes around 2-3 weeks. \n\n### Documents required to update the details on PAN Card\n\nTo update the information on the PAN card, kindly keep these documents ready.', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'}), Document(page_content='## Reprinting lost Aadhaar Card\n\nTo reprint your PAN card, you need to follow a specific procedure that involves providing certain documents and information to authenticate your identity. The process can take around 2-3 weeks to complete. You can apply for a reprint through ABC. We will guide you through the process and help you obtain a new copy of your PAN card.\n\n### Documents required for reprinting the lost PAN card', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'})]",
    "INR 2000/- Sources:[Document(page_content='Alternatively, you can also initiate the process on WhatsApp as well.\n\n### ABC fees to link PAN with Aadhaar\n\nThe charges for linking Pan & Aadhaar is INR 2000/-, including the penalty charges to be paid for the delay in linking Pan & Aadhaar.\n\n### Documents required to link PAN with Aadhaar\n\nKindly share a copy of your pan card and Aadhaar card. ABC will review the documents and share a payment link for the linking.', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'}), Document(page_content='### Charges for reprinting the PAN Card\n\nThe charges for reprinting the PAN Card are INR 2500 for e-pan, and INR 3700 for physical pan card.\n\n---\n\n## Linking PAN with Aadhaar card\n\nABC can link your PAN card and Aadhaar card on your behalf. \n\n### Process to link PAN with Aadhaar\n\n- Go to ABC app\n- Navigate to Services > NRI PAN Card > Link PAN with Aadhaar\n- Request reissue the required PAN card and make the payment\n- Our team will reach out to you for the required documents', metadata={'source': 'data\KnowledgeDocument(pan_card_services).txt'})]"
]

def evaluate_answers(questions, reference_answers, generated_answers):
    bleu_scores = []
    for i in range(len(questions)):
        reference = [reference_answers[i].split()]  # Convert reference answer to list of tokens
        generated = generated_answers[i].split()    # Convert generated answer to list of tokens

        # Calculate BLEU score for the current answer
        bleu = sentence_bleu(reference, generated)
        bleu_scores.append(bleu)

        # Print the evaluation result for each question-answer pair
        print(f"Question: {questions[i]}")
        print(f"Generated Answer: {generated_answers[i]}")
        print(f"Reference Answer: {reference_answers[i]}")
        print(f"BLEU Score: {bleu}")
        print("-" * 50)

    # Calculate the average BLEU score for all answers
    avg_bleu_score = sum(bleu_scores) / len(bleu_scores)
    print(f"Average BLEU Score: {avg_bleu_score}")

# Call the evaluation function
evaluate_answers(questions, reference_answers, generated_answers)
