# utils/target_scorer.py

def score_target(ip, ports_services):
    """
    Score a target based on common high-value services.
    More sensitive or exploitable services increase the score.
    """
    score = 0
    weight_map = {
        'ssh': 10,
        'http': 8,
        'https': 8,
        'ftp': 6,
        'mysql': 7,
        'rdp': 9,
        'smb': 10,
        'telnet': 6,
        'postgresql': 7,
        'vnc': 6,
        'redis': 8,
        'mongodb': 7,
        'unknown': 3,
    }

    for port, service in ports_services.items():
        normalized = service.lower()
        score += weight_map.get(normalized, 5)  # Default weight if unknown

    # Bonus: reward multiple exposed services
    if len(ports_services) >= 5:
        score += 10

    # Bonus: SSH + HTTP combo (indicative of admin panel?)
    if 'ssh' in ports_services.values() and 'http' in ports_services.values():
        score += 5

    return score
