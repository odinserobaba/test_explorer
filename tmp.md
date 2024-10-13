<!-- #region(collapsed) [NAME] -->
{{collapse(Версия (тест))
<pre>
    api-lc-license
    31bd869e dev 481269
    #132358  deploy/test-circuit  91a5bc9b 
    Evgeniy Serobaba

    lic-integratos
    6b75cafc rel 481269
    #132269  test-circuit  73188546 
    Evgeniy Serobaba
pre>
}}
<!-- #region(collapsed) [NAME] -->
* Шаг №1
{{collapse(Л-902 Заявление о выдаче лицензии ПХПРП_СХП)
https://lk-test.egais.ru/cabinet/licenses/inProcess/225439
* Довел до отрицального рещения по экспертизе документов. 
* Подписал уведомление о необходимости устранения в СЭД дело.
}}
<!-- #endregion --> 
<!-- #region(collapsed) [NAME] -->
* Шаг №2
{{collapse(В топик test-smev-leveler-in-response попало сообщение:)
<!-- #region(collapsed) [JSON] -->
<pre><code class='json'>
{
  "serviceId": "lic-integrator",
  "requestId": "7336bd13-8f3e-470b-96e1-ee561cfb1ab4",
  "requestType": "EPGU",
  "updateTimestamp": "2024-10-11T16:01:47.683+0300",
  "responseContent": {
    "serviceStatus": "2005",
    "caseNumber": "Л-902",
    "attachments": [
      {
        "path": "/mnt/leveler/storage/2024-10-11/72bd8439-87ce-11ef-81b2-da9d2b5bd730/notification.pdf"
      }
    ]
  }
}
</code></pre>
* Подписал на ЕПГУ Заявление об устрании выявленных нарушений
}}
<!-- #endregion --> 
<!-- #region(collapsed) [NAME] -->
* Шаг №3
{{collapse(В топик test-smev-leveler-in-request пришло сообщение:)
<!-- #region(collapsed) [JSON] -->
<pre><code class='json'>
{
  "id": "f22995d6-6c23-49c9-8857-ec0cc8e3fbaa",
  "serviceId": "lic-integrator",
  "requestId": "f77943c0-1eca-4fbc-a1de-0038f5c703f2",
  "requestType": "EPGU",
  "xsltId": 10,
  "responseId": "1f7447d6-ec7a-4fae-8bb9-f4f9508e5fa0",
  "messageId": "cb3daade-87a3-11ef-bc01-e69aa90b6245",
  "requestContent": {
    "epgu": {
      "orderID": "4650041559",
      "department": "100000012571",
      "serviceCode": "60009992",
      "targetCode": "60009992-1",
      "statementDate": "2024-10-11"
    },
    "applicant": {
      "ip": {
        "fullName": "",
        "shortName": "ИП Попова Д. А.",
        "lastName": "Попова",
        "firstName": "Дарья",
        "patronymic": "Алексеевна",
        "ogrnip": "310730882380772",
        "inn": "576853595470"
      },
      "address": "430013, Респ. Мордовия, г. Саранск, ул. Воинова, 10, 17",
      "email": "popova-da@fsrar.ru",
      "phone": "+7(917)5710200"
    },
    "agent": {
      "lastName": "",
      "firstName": "",
      "patronymic": "",
      "documentId": {
        "serial": "",
        "number": "",
        "issuerName": "",
        "issuerCode": "",
        "issueDate": ""
      },
      "dateOfBirth": "",
      "email": "",
      "phone": ""
    },
    "grant": {
      "subdivisions": [
        {
          "kpp": "",
          "address": "77:77:1111111:7777",
          "cadastralNumbers": {
            "warehouses": [
              {
                "warehouse": "77:77:1111111:7777"
              }
            ]
          },
          "parties": "",
          "subject": "",
          "startDate": "",
          "endDate": "",
          "equipment": "",
          "products": {
            "productNames": [
              {
                "productName": "вино"
              }
            ],
            "productNameText": ""
          },
          "kppHardwareTS": "",
          "addressHardwareTS": ""
        }
      ],
      "license": {
        "numOfYears": "4",
        "numOfMonths": "",
        "kindOfActivity": "Производство, хранение и поставки произведённой сельскохозяйственными производителями винодельческой продукции",
        "kindOfWork": ""
      },
      "laboratory": {
        "certificate": "1",
        "parties": "",
        "subject": "",
        "startDate": "",
        "endDate": ""
      },
      "bank": {
        "name": "",
        "account": ""
      },
      "payment": {
        "number": "1",
        "date": "2024-10-11",
        "amount": "",
        "purpose": ""
      },
      "uin": {
        "number": "",
        "date": ""
      },
      "vineyards": [
        {
          "cadastralNumber": "77:77:1111111:7777",
          "registrationNumber": "77:77:1111111:7777",
          "parties": "",
          "subject": "",
          "startDate": "",
          "endDate": ""
        }
      ]
    },
    "appliedDocuments": [
      {
        "name": "7841051711_86250.pdf",
        "businessName": "Документ, подтверждающий статус сельскохозяйственного товаропроизводителя",
        "type": "application/pdf",
        "mnemonic": "c181.FileUploadComponent.status_selhoz.4650041559"
      }
    ]
  },
  "requestTimestamp": "2024-10-11T10:39:58.304+0300",
  "updateTimestamp": "2024-10-11T10:39:58.866+0300",
  "kafkaPartition": 0,
  "kafkaOffset": 0,
  "route": "IN",
  "attachmentPath": "/mnt/leveler/storage/2024-10-11/cb3daade-87a3-11ef-bc01-e69aa90b6245/Application.zip",
  "state": "OUTGOING",
  "archivedStatus": true,
  "queuedStatus": true
}
</code></pre>
<!-- #endregion --> 
}}
<!-- #endregion --> 