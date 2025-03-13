import numpy as np


def assign_customers_to_representatives(customers, representatives, availability):
    """
    Zaman Karmaşıklığı: O(n * m)
    Burada n, müşteri sayısını, m ise temsilci sayısını ifade eder.
    Kodda her müşteri için tüm temsilciler kontrol edilerek en yakın temsilci seçilir, bu da O(n * m) zaman karmaşıklığına yol açar.

    Uzay Karmaşıklığı: O(n)
    Kodda yalnızca müşteri-temsilci eşleşmelerini tutan bir liste ve temsilcilerin kullanım durumu için bir set kullanılıyor.
    Bu nedenle uzay karmaşıklığı O(n) olur, çünkü sadece müşteri sayısı kadar veri saklanır.
    """

    n = len(customers)
    m = len(representatives)
    used_representatives = set()
    assignments = []
    total_distance = 0

    for customer in customers:
        min_distance = float('inf')
        assigned_rep = None
        for idx, rep in enumerate(representatives):
            if availability[idx] and idx not in used_representatives:
                distance = abs(customer - rep)
                if distance < min_distance:
                    min_distance = distance
                    assigned_rep = idx
        if assigned_rep is not None:
            assignments.append((customer, representatives[assigned_rep]))
            total_distance += min_distance
            used_representatives.add(assigned_rep)

    return total_distance, assignments


def select_marketing_campaigns(budget, costs, rois):
    """
    Zaman Karmaşıklığı: O(n * budget)
    Bu iki döngüde her kampanya için tüm bütçe değerleri kontrol ediliyor. İlk döngüde n kampanya üzerinde işlem yapılır,
    ve ikinci döngüde her bütçe için (budget) işlem yapılır. Bu nedenle toplam zaman karmaşıklığı O(n * budget) olur.

    Uzay Karmaşıklığı: O(n * budget)
    Dinamik programlama tablosu, n kampanya ve budget sütunları ile oluşturulmuştur.
    Bu nedenle uzay karmaşıklığı O(n * budget) olur.
    """
    n = len(costs)  # n kampanya sayısını alıyoruz

    dp = [0] * (budget + 1)
    selected = [[[] for _ in range(budget + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for b in range(budget, costs[i - 1] - 1, -1):

            if dp[b - costs[i - 1]] + rois[i - 1] > dp[b]:
                dp[b] = dp[b - costs[i - 1]] + rois[i - 1]
                selected[i][b] = selected[i - 1][b - costs[i - 1]] + [i - 1]
            else:
                selected[i][b] = selected[i - 1][b]

    selected_campaigns = [(costs[i], rois[i]) for i in selected[n][budget]]

    return dp[budget], selected_campaigns


budget = 10
costs = [3, 4, 5]
rois = [5, 6, 10]


# Test verileri
customers = [2, 5, 7]
representatives = [1, 6, 8]
availability = [True, True, False]  # Temsilcilerin uygunluk durumu

# Fonksiyonları çalıştır
customer_assignment_result, assignment_details = assign_customers_to_representatives(customers, representatives, availability)
marketing_campaign_result, selected_campaigns = select_marketing_campaigns(budget, costs, rois)

print("Müşteri Yönlendirme Sonucu (Toplam Mesafe):", customer_assignment_result)
print("Müşteri-Temsilci Eşleşmeleri:", assignment_details)
print("En İyi Pazarlama ROI:", marketing_campaign_result)
print("Seçilen Kampanyalar (Maliyet, ROI):", selected_campaigns)