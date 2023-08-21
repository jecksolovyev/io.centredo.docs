====================
Conversion rule info
====================

WDExtensions
============

WdExtensions - is a help java class for working with dictionaries inside XSLT map.
In order to apply it, the following namespace has to be added:

.. code:: xml

    <?xml version='1.0'?>
    <xsl:stylesheet version="1.0"
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                    xmlns:saxon="http://saxon.sf.net/"
                    xmlns:wdExtensions="java:com.whitedoc.xslt.extensions.WdExtensions"
                    exclude-result-prefixes="saxon wdExtensions">

There are 4 static methods:

| 1. wdExtensions:getValueFromDictionary(String dictionaryUuid, String columnByUuid, String valueToFind, String columnToFind)
| Can be used to find a value in column

| 2. wdExtensions:getRecordUuidByValueFromDictionary(String dictionaryUuid, String columnUuid, String valueToFind)
| Can be used to find UUID of dictionary record

| 3. wdExtensions:createAttachementWithSourceFile()
| Extension uploads original file to storage, creates attachment UUID and return UUID as result. This extension can be used if created envelope required original file. Each repetition of extension will create new attachment with new UUID.

| 4. wdExtensions:getMailboxUuidByAlias(String mailboxAlias)
| Extension accepts alias name and return mailboxUUID. Can be used to configure recipients in flow. Instead of mailboxAlias can be path to respective value in original document.

Conversion rule example for outgoing documents
==============================================

.. code:: xml

    <?xml version='1.0'?>
    <xsl:stylesheet version="1.0"
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                    xmlns:saxon="http://saxon.sf.net/"
                    xmlns:wdExtensions="java:com.whitedoc.xslt.extensions.WdExtensions"
                    exclude-result-prefixes="saxon wdExtensions">
        <xsl:output indent="yes"/>

        <xsl:template match="/">
            <xsl:apply-templates select="EDIFACT/ORDERS"/>
            <xsl:apply-templates select="EANCOM/ORDERS"/>
        </xsl:template>

        <xsl:template match="ORDERS">
            <xsl:variable name="supplierGLN" select="../UNB/UNB03/UNB0301"/>
            <xsl:variable name="senderGLN" select="../UNB/UNB02/UNB0201"/>
            <xsl:variable name="supplierUuid" select="{wdExtensions:getValueFromDictionary('a5390637-f3b5-49f3-b7f6-48132f6fe8bb', '7f9d20ab-71d8-45e0-9756-2887fd427cd6', $supplierGLN, 'f69ee017-1fb3-4ff1-a803-c4ade48ea65e')}"/>
            <envelope templateUuid="579ba3f3-7e26-4c7a-845c-ffa0fdf78057" templateVersion="55809865-32df-4341-91b0-b8bc44451394">
                <info>
                    <subject>Замовлення на постачання № <xsl:choose><!--Dlya MTI-->
                        <xsl:when test="../UNB/UNB02/UNB0201=4820140450000"><xsl:value-of select="BGM/BGM02/BGM0201"/></xsl:when>
                        <xsl:otherwise><xsl:value-of select="BGM/BGM02"/></xsl:otherwise>
                    </xsl:choose>
                    </subject>
                    <message>Оригінал замовлення</message>
                </info>
                <state>
                  <message/>
                  <date>
                    2021-02-03T12:22:52.709Z
                  </date>
                  <roleId>

                  </roleId>
                </state>
                <documents>
                    <document id="cd511754-cfd1-49a3-aae4-aab212d83cea">
                        <field name="NUMBER">
                            <xsl:choose><!--Dlya MTI-->
                                <xsl:when test="../UNB/UNB02/UNB0201=4820140450000"><xsl:value-of select="BGM/BGM02/BGM0201"/></xsl:when>
                                <xsl:otherwise><xsl:value-of select="BGM/BGM02"/></xsl:otherwise>
                            </xsl:choose>
                        </field>
                        <xsl:apply-templates select="DTM"/>
                        <xsl:apply-templates select="GROUP_2" mode="YC1"/>
                        <xsl:if test="GROUP_7/CUX/CUX01/CUX0102 and ../UNB/UNB03/UNB0301!='4829900003227'">
                            <field name="CURRENCY"><xsl:value-of select="GROUP_7/CUX/CUX01/CUX0102"/></field>
                        </xsl:if>
                        <xsl:choose>
                            <xsl:when test="GROUP_1/RFF/RFF01/RFF0102 and ../UNB/UNB02/UNB0201='4820086630009'">
                                <field name="INFO">№ акции: <xsl:value-of select="GROUP_1/RFF/RFF01/RFF0102"/></field>
                            </xsl:when>
                            <xsl:when test="../UNB/UNB02/UNB0201='4823060600005'">
                                <field name="INFO"><xsl:value-of select="FTX/FTX04/FTX0401"/>, <xsl:value-of select="FTX/FTX04/FTX0402"/>, <xsl:value-of select="FTX/FTX04/FTX0403"/></field>
                            </xsl:when>
                        </xsl:choose>
                        <xsl:apply-templates select="GROUP_2" mode="NAD"/>
                        <fieldgroup name="POSITION">
                            <xsl:choose>
                                <xsl:when test="../UNB/UNB03/UNB0301='4829900003227'">
                                    <xsl:apply-templates select="GROUP_28" mode="LOREAL"/>
                                </xsl:when>
                                <xsl:when test="GROUP_28">
                                    <xsl:apply-templates select="GROUP_28"/>
                                </xsl:when>
                                <xsl:otherwise>
                                    <xsl:apply-templates select="GROUP_25"/>
                                </xsl:otherwise>
                            </xsl:choose>
                        </fieldgroup>
                        <field name="POSITIONSCOUNT"><xsl:value-of select="count(//GROUP_28)"/></field>
                        <field name="SUMORDEREDQUANTITY"><xsl:value-of select="sum(//QTY0102)"/></field>
                    </document>
                </documents>
                <flow>
                    <roles>
                        <role id="f9378c46-5dfe-484a-b985-5a157d238b5c" mailboxUuid="625d1530-8896-49a5-b53c-37e5ade5e750"/>
                        <role id="d59d8545-f1d2-4008-951f-2f43509d966e" mailboxUuid="{$supplierUuid}"/>
                    </roles>
                </flow>
            </envelope>
        </xsl:template>

        <xsl:template match="DTM">
            <xsl:choose>
                <xsl:when test="DTM01/DTM0101 = '137'">
                    <field name="DATE">
                        <xsl:value-of select="substring(DTM01/DTM0102, 7, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 5, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 1, 4)"/>
                    </field>
                </xsl:when>
                <xsl:when test="DTM01/DTM0101 = '2'">
                    <xsl:if test="string-length(DTM01/DTM0102) = '12'">
                        <field name="DELIVERYDATE">
                            <xsl:value-of select="substring(DTM01/DTM0102, 7, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 5, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 1, 4)"/>
                        </field>
                    </xsl:if>
                    <xsl:if test="string-length(DTM01/DTM0102) = '8'">
                        <field name="DELIVERYDATE">
                            <xsl:value-of select="substring(DTM01/DTM0102, 7, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 5, 2)"/>-<xsl:value-of select="substring(DTM01/DTM0102, 1, 4)"/>
                        </field>
                    </xsl:if>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="GROUP_2" mode="YC1">
            <xsl:choose>
                <xsl:when test="NAD/NAD01 = 'SU'">
                    <xsl:if test="NAD/NAD03">
                        <field name="CAMPAIGNNUMBER">
                            <xsl:value-of select="NAD/NAD03"/>
                        </field>
                    </xsl:if> <xsl:apply-templates select="GROUP_3" mode="YC1"/>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="GROUP_3" mode="YC1">
            <xsl:choose>
                <xsl:when test="RFF/RFF01/RFF0101='YC1'">
                    <field name="CAMPAIGNNUMBER">
                        <xsl:value-of select="RFF/RFF01/RFF0102"/>
                    </field>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="GROUP_2" mode="NAD">
            <xsl:choose>
                <xsl:when test="NAD/NAD01='SU'">
                    <xsl:variable name="supplierRecordValue" select="NAD/NAD02/NAD0201"></xsl:variable>
                    <field name="SUPPLIER" recordUuid="{wdExtensions:getRecordUuidByValueFromDictionary('a5390637-f3b5-49f3-b7f6-48132f6fe8bb', '7f9d20ab-71d8-45e0-9756-2887fd427cd6', $supplierRecordValue)}">
                        <xsl:value-of select="$supplierRecordValue"/>
                    </field>
                </xsl:when>
                <xsl:when test="NAD/NAD01='BY'">
                    <xsl:variable name="buyer" select="string-length(NAD/NAD02/NAD0201)"/>
                    <xsl:choose>
                        <xsl:when test="$buyer=13">
                            <xsl:variable name="buyerRecordValue" select="NAD/NAD02/NAD0201"></xsl:variable>
                            <field name="BUYER" recordUuid="{wdExtensions:getRecordUuidByValueFromDictionary('258a20bd-ffe5-47b4-a76a-5d440469e444', '592553ba-3e02-43c1-bff6-b7fa438b8fda', $buyerRecordValue)}">
                                <xsl:value-of select="$buyerRecordValue"/>
                            </field>
                        </xsl:when>
                        <xsl:otherwise>
                            <field name="BUYERCODE">
                                <xsl:value-of select="NAD/NAD02/NAD0201"/>
                            </field>
                        </xsl:otherwise>
                    </xsl:choose>
                </xsl:when>
                <xsl:when test="NAD/NAD01='DP'">
                    <xsl:variable name="deliveryPlaceValue" select="NAD/NAD02/NAD0201"></xsl:variable>
                    <field name="DELIVERYPLACE" recordUuid="{wdExtensions:getRecordUuidByValueFromDictionary('258a20bd-ffe5-47b4-a76a-5d440469e444', '592553ba-3e02-43c1-bff6-b7fa438b8fda', $deliveryPlaceValue)}">
                        <xsl:value-of select="$deliveryPlaceValue"/>
                    </field>
                </xsl:when>
                <xsl:when test="NAD/NAD01='IV'">
                    <xsl:variable name="invoicePartnerRecordValue" select="NAD/NAD02/NAD0201"></xsl:variable>
                    <field name="INVOICEPARTNER" recordUuid="{wdExtensions:getRecordUuidByValueFromDictionary('258a20bd-ffe5-47b4-a76a-5d440469e444', '592553ba-3e02-43c1-bff6-b7fa438b8fda', $invoicePartnerRecordValue)}">
                        <xsl:value-of select="$invoicePartnerRecordValue"/>
                    </field>
                </xsl:when>
                <xsl:when test="NAD/NAD01='CA'">
                    <xsl:if test="NAD/NAD02/NAD0201">
                        <xsl:if test="13>string-length(NAD/NAD02/NAD0201)">
                            <field name="RECIPIENTCODE">
                                <xsl:value-of select="NAD/NAD02/NAD0201"/>
                            </field>
                        </xsl:if>
                    </xsl:if>
                    <xsl:if test="NAD/NAD05">
                        <field name="RECIPIENTADRESS">
                            <xsl:value-of select="NAD/NAD05"/>
                        </field>
                    </xsl:if>
                    <xsl:if test="NAD/NAD06">
                        <field name="RECIPIENTCITY">
                            <xsl:value-of select="NAD/NAD06"/>
                        </field>
                    </xsl:if>
                    <xsl:if test="NAD/NAD04">
                        <field name="RECIPIENTNAME">
                            <xsl:value-of select="NAD/NAD04"/>
                        </field>
                    </xsl:if>
                </xsl:when>
                <xsl:when test="NAD/NAD01='CL'">
                    <field name="INVOICEPARTNER">
                        <xsl:value-of select="NAD/NAD02/NAD0201"/>
                    </field>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="GROUP_28">
            <fieldset index="{position() - 1}">
                <field name="POSITIONNUMBER">
                    <xsl:value-of select="position()"/>
                </field>
                <xsl:choose>
                    <xsl:when test="boolean(LIN/LIN03/LIN0301)">
                        <field name="PRODUCT">
                            <xsl:value-of select="LIN/LIN03/LIN0301"/>
                        </field>
                    </xsl:when>
                    <xsl:otherwise>
                        <field name="PRODUCT">4829090909095</field>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:apply-templates select="PIA"/>
                <xsl:apply-templates select="QTY"/>
                <xsl:choose>
                    <xsl:when test="GROUP_32/PRI/PRI01/PRI0101 = 'AAA' and boolean(substring-before(GROUP_32/PRI/PRI01/PRI0102, '.'))">
                        <field name="ORDERPRICE">
                            <xsl:value-of select="substring-before(GROUP_32/PRI/PRI01/PRI0102, '.')"/>.<xsl:value-of select="substring(substring-after(GROUP_32/PRI/PRI01/PRI0102, '.'), 1, 3)"/>
                        </field>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:if test="GROUP_32/PRI/PRI01/PRI0101 = 'AAA'">
                            <field name="ORDERPRICE">
                                <xsl:value-of select="GROUP_32/PRI/PRI01/PRI0102"/>
                            </field>
                        </xsl:if>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:choose>
                    <xsl:when test="IMD/IMD03/IMD0304">
                        <field name="CHARACTERISTIC_DESCRIPTION">
                            <xsl:value-of select="translate(IMD/IMD03/IMD0304, '&amp;&lt;&gt;', '')"/><xsl:if test="boolean(IMD03/IMD0305)">(<xsl:value-of select="translate(IMD03/IMD0305, '&amp;&lt;&gt;', '')"/>)</xsl:if>
                        </field>
                    </xsl:when>
                </xsl:choose>
                <xsl:if test="FTX"><xsl:apply-templates select="FTX"/></xsl:if>
            </fieldset>
        </xsl:template>

        <xsl:template match="GROUP_28" mode="LOREAL">
            <fieldset index="{position() - 1}">
                <field name="POSITIONNUMBER">
                    <xsl:value-of select="position()"/>
                </field>
                <xsl:choose>
                    <xsl:when test="boolean(LIN/LIN03/LIN0301)">
                        <field name="PRODUCT">
                            <xsl:value-of select="LIN/LIN03/LIN0301"/>
                        </field>
                    </xsl:when>
                    <xsl:otherwise>
                        <field name="PRODUCT">4829090909095</field>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:apply-templates select="PIA" mode="LOREAL"/>
                <xsl:apply-templates select="QTY" mode="LOREAL"/>
            </fieldset>
        </xsl:template>

        <xsl:template match="GROUP_25">
            <fieldset index="{position() - 1}">
                <field name="POSITIONNUMBER">
                    <xsl:value-of select="position()"/>
                </field>
                <xsl:choose>
                    <xsl:when test="boolean(LIN/LIN03/LIN0301)">
                        <field name="PRODUCT">
                            <xsl:value-of select="LIN/LIN03/LIN0301"/>
                        </field>
                    </xsl:when>
                    <xsl:otherwise>
                        <field name="PRODUCT">4829090909095</field>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:apply-templates select="PIA"/>
                <xsl:apply-templates select="QTY"/>
                <xsl:choose>
                    <xsl:when test="GROUP_32/PRI/PRI01/PRI0101 = 'AAA' and boolean(substring-before(GROUP_32/PRI/PRI01/PRI0102, '.'))">
                        <field name="ORDERPRICE">
                            <xsl:value-of select="substring-before(GROUP_32/PRI/PRI01/PRI0102, '.')"/>.<xsl:value-of select="substring(substring-after(GROUP_32/PRI/PRI01/PRI0102, '.'), 1, 3)"/>
                        </field>
                    </xsl:when>
                    <xsl:when test="GROUP_28/PRI/PRI01/PRI0101 = 'AAA' and boolean(substring-before(GROUP_28/PRI/PRI01/PRI0102, '.'))">
                        <field name="ORDERPRICE">
                            <xsl:value-of select="substring-before(GROUP_28/PRI/PRI01/PRI0102, '.')"/>.<xsl:value-of select="substring(substring-after(GROUP_28/PRI/PRI01/PRI0102, '.'), 1, 3)"/>
                        </field>
                    </xsl:when>
                    <xsl:otherwise>
                        <xsl:if test="GROUP_32/PRI/PRI01/PRI0101 = 'AAA'">
                            <field name="ORDERPRICE">
                                <xsl:value-of select="GROUP_32/PRI/PRI01/PRI0102"/>
                            </field>
                        </xsl:if>
                        <xsl:if test="GROUP_28/PRI/PRI01/PRI0101 = 'AAA'">
                            <field name="ORDERPRICE">
                                <xsl:value-of select="GROUP_28/PRI/PRI01/PRI0102"/>
                            </field>
                        </xsl:if>
                    </xsl:otherwise>
                </xsl:choose>
                <xsl:choose>
                    <xsl:when test="IMD/IMD03/IMD0304">
                        <field name="CHARACTERISTIC_DESCRIPTION">
                            <xsl:value-of select="translate(IMD/IMD03/IMD0304, '&amp;&lt;&gt;', '')"/><xsl:if test="boolean(IMD/IMD03/IMD0305)">(<xsl:value-of select="translate(IMD/IMD03/IMD0305, '&amp;&lt;&gt;', '')"/>)</xsl:if>
                        </field>
                    </xsl:when>
                </xsl:choose>
            </fieldset>
        </xsl:template>

        <xsl:template match="PIA">
            <xsl:choose>
                <xsl:when test="PIA01 = '1'">
                    <xsl:if test="PIA02/PIA0202 = 'IN' or PIA02/PIA0202 = 'BP'">
                        <field name="PRODUCTIDBUYER">
                            <xsl:value-of select="PIA02/PIA0201"/>
                        </field>
                    </xsl:if>
                    <xsl:if test="PIA02/PIA0202 = 'SA'">
                        <field name="PRODUCTIDSUPPLIER">
                            <xsl:value-of select="PIA02/PIA0201"/>
                        </field>
                    </xsl:if>
                </xsl:when>
                <xsl:when test="PIA01 = '5'">
                    <xsl:if test="PIA02/PIA0202 = 'IN' or PIA02/PIA0202 = 'BP'">
                        <field name="BUYERPARTNUMBER">
                            <xsl:value-of select="PIA02/PIA0201"/>
                        </field>
                    </xsl:if>
                </xsl:when>
            </xsl:choose>
        </xsl:template>
        <xsl:template match="PIA" mode="LOREAL">
            <xsl:choose>
                <xsl:when test="PIA01 = '5'">
                    <xsl:if test="PIA02/PIA0202 = 'IN' or PIA02/PIA0202 = 'BP'">
                        <field name="PRODUCTIDBUYER">
                            <xsl:value-of select="PIA02/PIA0201"/>
                        </field>
                    </xsl:if>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="QTY">
            <xsl:choose>
                <xsl:when test="QTY01/QTY0101 = '21'">
                    <field name="ORDEREDQUANTITY">
                        <xsl:value-of select="QTY01/QTY0102"/>
                    </field>
                    <xsl:if test="boolean(QTY01/QTY0103)">
                        <field name="ORDERUNIT">
                            <xsl:variable name="orderUnitValue" select="QTY01/QTY0103"/>
                            <xsl:value-of select="wdExtensions:getValueFromDictionary('ee0aeb8e-ba06-41c7-8851-8ac38874fd4b', '52140044-da47-4cf9-90c6-988f44499d11', $orderUnitValue, '7aa2b0d9-bb42-4a4f-8588-46cfa4eda07c')"/>
                        </field>
                    </xsl:if>
                </xsl:when>
                <xsl:when test="QTY01/QTY0101 = '59'">
                    <field name="QUANTITYOFCUINTU">
                        <xsl:value-of select="QTY01/QTY0102"/>
                    </field>
                </xsl:when>
            </xsl:choose>
        </xsl:template>
        <xsl:template match="QTY" mode="LOREAL">
            <xsl:choose>
                <xsl:when test="QTY01/QTY0101 = '21'">
                    <field name="ORDEREDQUANTITY">
                        <xsl:value-of select="QTY01/QTY0102"/>
                    </field>
                    <xsl:if test="boolean(QTY01/QTY0103)">
                        <field name="ORDERUNIT">
                            <xsl:variable name="orderUnitValue" select="QTY01/QTY0103"/>
                            <xsl:value-of select="wdExtensions:getValueFromDictionary('ee0aeb8e-ba06-41c7-8851-8ac38874fd4b', '52140044-da47-4cf9-90c6-988f44499d11', $orderUnitValue, '7aa2b0d9-bb42-4a4f-8588-46cfa4eda07c')"/>
                        </field>
                    </xsl:if>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="FTX">
            <xsl:choose>
                <xsl:when test="FTX01='QQD'">
                    <field name="CONDITIONSTATUS">
                        <xsl:value-of select="FTX04"/>
                    </field>
                </xsl:when>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="GROUP_2" mode="NADUP">
            <xsl:if test="NAD/NAD01='DP'">
                <xsl:choose>
                    <xsl:when test="NAD/NAD02/NAD0201 = 'xxxxxxxxxxxxx'">xxxxxxxxxxxxx</xsl:when>
                    <xsl:otherwise>9099999104043</xsl:otherwise>
                </xsl:choose>
            </xsl:if>
        </xsl:template>

    </xsl:stylesheet>
	
XLS and X12 to XML conversion
=============================

Our platform has capabilities to convert .xls and .xlsx files and X12 files (.xml or .txt) to envelopes. This is achieved by using built-in converter. To use it you should use sample of needed format file as sourse file in new conversion rule (first window). After that you have to write conversion rule in second window (use Xpath to extract needed values to according fields). Then try running your rule - you should see output in 3rd window. Do not forget to add regexp to name field so correct files can be found for conversion. When conversion rule is created, You can put needed files with accorrding names directly to your outbox or coutbox folders and they wil be converted to envelopes automatically.

Conversion rule example for incoming documents
==============================================

.. code:: xml

    <?xml version="1.0" encoding="ISO-8859-5"?>
    <xsl:stylesheet version="1.0"
                    xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
                    xmlns:uuid="java:java.util.UUID"
                    xmlns:saxon="http://saxon.sf.net/"
                    xmlns:wdExtensions="java:com.whitedoc.xslt.extensions.WdExtensions"
                    exclude-result-prefixes="saxon wdExtensions">
        <xsl:output indent="yes" omit-xml-declaration="yes" encoding="ISO-8859-5" method="text"/>
        <xsl:variable name="uid" select="uuid:randomUUID()"/>
        <xsl:param name="senderMailboxUuid" select="envelope/flow/roles/role[1]/@mailboxUuid"/>
        <xsl:param name="recipientMailboxUuid" select="envelope/flow/roles/role[2]/@mailboxUuid"/>
        <xsl:variable name="senderGLN" select="wdExtensions:getValueFromDictionary('5bc5be5a-751d-4ae3-8ad8-3a6ac1ab71c8', '1ddf9e46-49f5-41a2-b6f5-7c3015bc4505', $senderMailboxUuid, '4f68fbf0-d78d-4aef-9192-bccd0c8d6011')"/>
        <xsl:variable name="recipientGLN" select="wdExtensions:getValueFromDictionary('5bc5be5a-751d-4ae3-8ad8-3a6ac1ab71c8', '1ddf9e46-49f5-41a2-b6f5-7c3015bc4505', $recipientMailboxUuid, '4f68fbf0-d78d-4aef-9192-bccd0c8d6011')"/>
        <xsl:template match="/">
            <xsl:apply-templates select="envelope/documents/document"/>
        </xsl:template>
        <xsl:template match="document">
            <xsl:choose>
                <xsl:when test="$recipientGLN='4820086639637'">
                    <xsl:call-template name="DESADV"/>
                </xsl:when>
                <xsl:when test="$recipientGLN='4820086630009'">
                    <xsl:call-template name="DESADV"/>
                </xsl:when>
            </xsl:choose>
        </xsl:template>
        <xsl:template name="DESADV">
            <xsl:param name="date" select="field[@name='DATE']"/>
            <xsl:param name="Orderdate" select="field[@name='ORDERDATE']"/>
            <xsl:choose>
                <xsl:when test="$senderGLN=('4820110633693','4820110633785','9863521000093','9863521003131','9863521004022','9863521004015','9863521008150')">Lasynia wrong</xsl:when>
                <xsl:otherwise>
                    <xsl:choose>
                        <xsl:when test="$senderGLN='4824025030288'">UNB+UNOC:3+4829900005924</xsl:when>
                        <xsl:when test="$senderGLN='9863521027830'">UNB+UNOC:3+4829900006907</xsl:when>
                        <xsl:when test="$senderGLN='9863521030045'">UNB+UNOC:3+4829900006891</xsl:when>
                        <xsl:when test="$senderGLN='4820110631736'">UNB+UNOC:3+9863571155385</xsl:when>
                        <xsl:when test="$senderGLN='9864082514562'">UNB+UNOC:3+4829900015633</xsl:when>
                        <xsl:otherwise>UNA:+.? '
                        UNB+UNOE:3+<xsl:value-of select="$senderGLN"/></xsl:otherwise>
                            </xsl:choose>:14+<xsl:value-of select="$recipientGLN"/>:14+<xsl:value-of select="translate(substring($date, 3, 8), '-', '')"/>:0000+<xsl:value-of select="substring(translate($uid,'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-',''),1,14)"/><xsl:call-template name="TESTFLAGREAL"/>'
                            UNH+<xsl:value-of select="substring(translate(field[@name='NUMBER'], '№ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-#!@$%^*№()-_=+:;', ''),1,14)"/>+DESADV:D:01B:UN:EAN007'
                            BGM+351+<xsl:value-of select="field[@name='NUMBER']"/>+9'
                            DTM+137:<xsl:value-of select="translate($date, '-', '')"/>:102'<xsl:choose><xsl:when test="$recipientGLN='4820086639637'">
                            DTM+17:<xsl:value-of select="translate(field[@name='DELIVERYDATE'], '-', '')"/><xsl:value-of select="translate(field[@name='DELIVERYTIME'], ':', '')"/>:203'</xsl:when><xsl:otherwise>
                            DTM+17:<xsl:value-of select="translate(field[@name='DELIVERYDATE'], '-', '')"/>:102'</xsl:otherwise></xsl:choose><xsl:if test="field[@name='ORDERNUMBER']">
                            RFF+ON:<xsl:value-of select="substring(field[@name='ORDERNUMBER'], 1, 15)"/>'</xsl:if>
                            DTM+171:<xsl:value-of select="translate($Orderdate, '-', '')"/>:102'<xsl:if test="boolean(field[@name='DELIVERYNOTENUMBER'])">
                            RFF+DQ:<xsl:value-of select="substring(field[@name='DELIVERYNOTENUMBER'], 1, 15)"/>'</xsl:if>
                            NAD+BY+<xsl:value-of select="normalize-space(field[@name='BUYER'])"/>::9'
                            NAD+SU+<xsl:value-of select="normalize-space(field[@name='SUPPLIER'])"/>::9'<xsl:if test="field[@name='CAMPAIGNNUMBER']">
                            RFF+YC1:<xsl:value-of select="field[@name='CAMPAIGNNUMBER']"/>'</xsl:if>
                            NAD+DP+<xsl:value-of select="normalize-space(field[@name='DELIVERYPLACE'])"/>::9'
                            CPS+1'<xsl:if test="field[@name='TOTALPALLETS']">
                            PAC+<xsl:value-of select="field[@name='TOTALPALLETS']"/>++201::9'</xsl:if><xsl:if test="field[@name='TOTALPACKAGES']">
                            PAC+<xsl:value-of select="field[@name='TOTALPACKAGES']"/>++PK'</xsl:if><xsl:apply-templates select="fieldgroup[@name='PACKINGSEQUENCE']/fieldset" mode="ALL"/></xsl:otherwise>
            </xsl:choose>
            <xsl:choose>
                <xsl:when test="field/@name='BUYER' and field='4824025000007'">UNT+<xsl:call-template name="KONTRCIFRABILLA"/>+<xsl:value-of select="substring(translate(field[@name='NUMBER'], '№ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-#!@$%^*()-_=+:;', ''), 1, 14)"/>'UNZ+1+<xsl:value-of select="substring(translate($uid,'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-',''),1,14)"/>'</xsl:when>
                <xsl:when test="$senderGLN='4829900002626'">
                    <xsl:if test="field[@name='TOTALPACKAGES']">CNT+11:<xsl:value-of select="field[@name='TOTALPACKAGES']"/>'</xsl:if>UNT+<xsl:call-template name="KONTRCIFRA_MTI"/>+<xsl:value-of select="substring(translate(field[@name='NUMBER'], '№ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-#!@$%^*()-_=+:;', ''),1,14)"/>'
                    UNZ+1+<xsl:value-of select="substring(translate($uid,'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-',''),1,14)"/>'</xsl:when>
                <xsl:otherwise>
                UNT+<xsl:if test="boolean(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='ORDEREDQUANTITY'])"><xsl:call-template name="KONTRCIFRA"/></xsl:if><xsl:if test="not(boolean(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='ORDEREDQUANTITY']))"><xsl:call-template name="KONTRCIFRA_BEZ_ORDEREDQUANTITY"/></xsl:if>+<xsl:value-of select="substring(translate(field[@name='NUMBER'], '№ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-#!@$%^*()-_=+:;', ''),1,14)"/>'
                UNZ+1+<xsl:value-of select="substring(translate($uid,'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-',''),1,14)"/>'</xsl:otherwise>
            </xsl:choose>
        </xsl:template>

        <xsl:template match="fieldgroup[@name='PACKINGSEQUENCE']/fieldset" mode="BILLA">LIN+<xsl:value-of select="position()"/>++<xsl:value-of select="translate(field[@name='PRODUCT'], ' ','')"/>:SRV'<xsl:if test="boolean(field[@name='PRODUCTIDBUYER'])">PIA+1+<xsl:value-of select="field[@name='PRODUCTIDBUYER']"/>:IN::92'</xsl:if><xsl:if test="boolean(field[@name='PRODUCTIDSUPPLIER'])">PIA+1+<xsl:value-of select="field[@name='PRODUCTIDSUPPLIER']"/>:SU::92'</xsl:if>QTY+12:<xsl:value-of select="field[@name='DELIVEREDQUANTITY']"/><xsl:if test="field/@name='DELIVEREDUNIT' and field='KGM'">:KGM</xsl:if>'<xsl:if test="boolean(field[@name='ORDEREDQUANTITY'])">QTY+21:<xsl:value-of select="field[@name='ORDEREDQUANTITY']"/>'</xsl:if></xsl:template>

        <xsl:template match="fieldgroup[@name='PACKINGSEQUENCE']/fieldset" mode="ALL">
        LIN+<xsl:value-of select="position()"/>++<xsl:value-of select="translate(field[@name='PRODUCT'], ' ','')"/>:SRV'<xsl:if test="boolean(field[@name='PRODUCTIDBUYER'])">
        PIA+1+<xsl:value-of select="field[@name='PRODUCTIDBUYER']"/>:IN::92'</xsl:if><xsl:if test="field[@name='PACKAGEID']">
        PIA+1+<xsl:value-of select="field[@name='PACKAGEID']"/>:CG::92'</xsl:if><xsl:choose><xsl:when test="field[@name='DELIVERYQUANTITY']">
        QTY+12:<xsl:value-of select="field[@name='DELIVERYQUANTITY']"/><xsl:if test="field/@name='DELIVEREDUNIT' and field='KGM'">:KGM</xsl:if>'</xsl:when><xsl:otherwise>
        QTY+12:<xsl:value-of select="field[@name='DELIVEREDQUANTITY']"/><xsl:if test="field/@name='DELIVEREDUNIT' and field='KGM'">:KGM</xsl:if>'</xsl:otherwise></xsl:choose><xsl:choose><xsl:when test="string-length(field[@name='ORDEREDQUANTITY'])!=0">
        QTY+21:<xsl:value-of select="field[@name='ORDEREDQUANTITY']"/>'</xsl:when><xsl:otherwise>
        QTY+21:<xsl:value-of select="field[@name='DELIVEREDQUANTITY']"/>'</xsl:otherwise></xsl:choose><!--<xsl:if test="DESCRIPTION">
        FTX+DEL+1+002+<xsl:value-of select="DESCRIPTION"/>'</xsl:if>--><xsl:if test="field[@name='CONDITIONSTATUS']">
        FTX+QQD+1+002+<xsl:value-of select="field[@name='CONDITIONSTATUS']"/>'</xsl:if></xsl:template>


        <xsl:template name="KONTRCIFRA">

            <xsl:value-of select="10 + count(field[@name='CAMPAIGNNUMBER']) + count(field[@name='TOTALPACKAGES']) + count(field[@name='TOTALPALLETS']) +  count(field[@name='DELIVERYNOTENUMBER']) +   count(field[@name='DELIVERYPLACE']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCT']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCTIDBUYER']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DELIVEREDQUANTITY']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='ORDEREDQUANTITY'])  "/>
        </xsl:template>

        <xsl:template name="KONTRCIFRA_BEZ_ORDEREDQUANTITY">
            <xsl:value-of select="10 +    count(field[@name='DELIVERYNOTENUMBER']) +   count(field[@name='DELIVERYPLACE']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCT']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCTIDBUYER']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DELIVEREDQUANTITY']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DELIVEREDQUANTITY'])   "/>
        </xsl:template>

        <xsl:template name="KONTRCIFRABILLA">

            <xsl:value-of select="11 +    count(field[@name='DELIVERYNOTENUMBER']) +   count(field[@name='DELIVERYPLACE']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCT']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCTIDBUYER']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DELIVEREDQUANTITY']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='ORDEREDQUANTITY'])  "/>
        </xsl:template>

        <xsl:template name="KONTRCIFRA_MTI">

            <xsl:value-of select="3 +   count(field[@name='NUMBER']) +   count(field[@name='DATE']) +   count(field[@name='DELIVERYDATE']) +   count(field[@name='ORDERNUMBER']) +   count(field[@name='ORDERDATE']) +   count(field[@name='DELIVERYNOTENUMBER']) +   count(field[@name='BUYER']) +   count(field[@name='BUYERCODE']) +   count(field[@name='SUPPLIER']) +   count(field[@name='DELIVERYPLACE']) +   count($senderGLN) +   count(field[@name='SENDERNAME']) +   count(field[@name='SENDERPHONE']) +   count(field[@name='INFO']) +   count(field[@name='TRANSPORTID']) +    count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCT']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCTIDBUYER']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PRODUCTIDSUPPLIER']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DELIVEREDQUANTITY']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='ORDEREDQUANTITY']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='DESCRIPTION']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='CONDITIONSTATUS']) +   count(fieldgroup[@name='PACKINGSEQUENCE']/fieldset/field[@name='PACKAGEID'])+    count(field[@name='TOTALPACKAGES'])   "/>
        </xsl:template>

        <xsl:template name="DATEPLUS1">
            <xsl:variable name="Date" select="field[@name='DATE']"/>
            <xsl:variable name="Plus" select="translate($Date, '-', '')"/>
            <xsl:choose>
                <xsl:when test="substring($Plus,5,4) = 0228">20100301</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0331">20100401</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0430">20100501</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0531">20100601</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0630">20100701</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0731">20100801</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0831">20100901</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 0930">20101001</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 1031">20101101</xsl:when>
                <xsl:when test="substring($Plus,5,4) = 1130">20101201</xsl:when>
                <xsl:when test="$Plus = 20091231">20100101</xsl:when>
                <xsl:when test="$Plus = 20101231">20110101</xsl:when>
                <xsl:otherwise>
                    <xsl:variable name="Char" select="$Plus+1"/>
                    <xsl:variable name="Transform" select="translate($Char,'.', '')"/>
                    <xsl:value-of select="substring($Transform,1,8)"/>
                </xsl:otherwise>
            </xsl:choose>
        </xsl:template>


        <xsl:template name="NUMB1">
            <xsl:variable name="literals">+?"'&amp;&lt;&gt;</xsl:variable>
            <xsl:value-of select="substring(translate(field[@name='NUMBER'], 'ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-№#!@$%^*№()-_=+:;', ''), $literals, '')"/>
        </xsl:template>

        <xsl:template name="NUMB">
            <xsl:value-of select="translate(field[@name='NUMBER'], 'ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-№#!@$%^*№()-_=+:;', '')"/>
        </xsl:template>

        <xsl:template name="DELIVERYNOTENUMBER">
            <xsl:value-of select="translate(field[@name='DELIVERYNOTENUMBER'], 'ІіЙйЦцУуКкЕеНнГгШшЩщЗзХхЪъЭэЖжДдЛлОоРрПпАаВвЫыФфЯяЧчСсМмИиТтЬьБбЮюЁёЇїЄє AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz-№#!@$%^*№()-_=+:;', '')"/>
        </xsl:template>

        <xsl:template name="TESTFLAGREAL">
            <xsl:choose>
                <xsl:when test="$recipientGLN='4820086630009'"></xsl:when>
                <xsl:when test="$recipientGLN='4820086639637'"></xsl:when>
                <xsl:otherwise>++++++1</xsl:otherwise>
            </xsl:choose>
        </xsl:template>
    </xsl:stylesheet>