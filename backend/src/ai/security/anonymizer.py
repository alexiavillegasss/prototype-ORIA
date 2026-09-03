import re

class Anonymizer:
    def __init__(self):
        # Regex to detect titles and subsequent capitalized proper names (handles French accents and hyphens)
        # Matches Mme, M., Mr., Mlle, Madame, Monsieur, Mademoiselle
        # Note: No trailing \b after the titles group so that M. (which ends in a dot) matches correctly!
        self.title_pattern = re.compile(
            r'\b(Mme|M\.|Mr\.|Mlle|Madame|Monsieur|Mademoiselle)\s+([A-Z\u00c0-\u00dc][a-zA-Z\u00c0-\u00df\u00e0-\u00f6\u00f8-\u00ff\s\-\'\b]+)',
            re.UNICODE
        )
        
        # Words that might be capitalized but are actually verbs/pronouns/common words, NOT names
        self.ignored_words = {
            "Vit", "Est", "Elle", "Il", "Habite", "A", "Ont", "S'en", "Ses", 
            "Son", "Sa", "Leur", "Leurs", "Qui", "Que", "Mais", "Ou", "Et", 
            "Donc", "Or", "Ni", "Car", "Dans", "Pour", "Avec", "Chez", "Par"
        }
        
        # Regex d'anonymisation des adresses physiques exactes (ex: 18 rue des mimosas, 53 impasse Blériot)
        self.address_pattern = re.compile(
            r'\b(?:\d{1,4}\s*(?:bis|ter|quater|[a-c])?\s*,?\s*)?(?:rue|avenue|av\.?|bd\.?|boulevard|impasse|chemin|allée|allee|(?<!en\s)(?<!mettre\s)(?<!mise\s)place|route|résidence|residence|square|passage|quai|cours)\s+[^,\.\;\n]+?(?=\s+(?:à|a|au|en|sur|\b\d{5}\b|\.|\,|\;|\n|$))',
            re.IGNORECASE | re.UNICODE
        )
        
    def pseudonymize(self, text: str) -> str:
        """
        Anonymizes proper names and street addresses in a clinical description.
        Example:
            "Mme Antoinette Durand, 88 ans, 18 rue des mimosas à La Seyne..." 
            -> "Mme A. D., 88 ans, [ADRESSE ANONYMISÉE] à La Seyne..."
        """
        if not text:
            return text

        def replace_name(match):
            title = match.group(1)
            full_name = match.group(2).strip()
            
            # Split by whitespace, hyphens or apostrophes to handle complex names (e.g. Jean-Pierre, De L'Alba)
            name_parts = re.split(r'[\s\-\']+', full_name)
            
            valid_parts = []
            for part in name_parts:
                # Clean punctuation from the end of the word
                cleaned_part = re.sub(r'[^\w\u00c0-\u00dc]', '', part)
                
                # Check if it starts with an uppercase letter and is not an ignored word
                if cleaned_part and cleaned_part[0].isupper() and cleaned_part not in self.ignored_words:
                    valid_parts.append(cleaned_part)
                else:
                    # As soon as we find a non-name word, stop accumulating name parts
                    break
                    
            if not valid_parts:
                return match.group(0)
                
            # Reconstruct with initials
            initials = [f"{part[0]}." for part in valid_parts]
            pseudonym = f"{title} {' '.join(initials)}"
            
            # Calculate exactly how much of the original string was matched and converted to initials
            matched_substring_pattern = r'^' + r'[\s\-\']+'.join(re.escape(p) for p in valid_parts)
            sub_match = re.search(matched_substring_pattern, full_name)
            
            if sub_match:
                matched_len = sub_match.end()
                remaining = full_name[matched_len:]
                return pseudonym + remaining
            else:
                return pseudonym

        text = self.title_pattern.sub(replace_name, text)
        text = self.address_pattern.sub("[ADRESSE ANONYMISÉE]", text)
        return text
