PLACEHOLDER = "[name]"

with open("MailMerging/names.txt") as names_file:
  names= names_file.readlines()

with open("MailMerging/starting_letter.docx") as letter:
    content=letter.read()
    for name in names:
      stripped_name=name.strip()
      new_letter= content.replace(PLACEHOLDER, stripped_name)

      with open(f"MailMerging/OutputLetters/letter_for_{stripped_name}.docx", mode='w') as completed_letter:
         completed_letter.write(new_letter)
   