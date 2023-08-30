===================
Document management
===================

This section describes all functionality of document editor. Document editor page contain the following data:

.. image:: pic_documentManagement/documentEditor.png
   :width: 1440
   :align: center

1. **Documents management menu** allows to view, create, reorder and delete documents inside the template
2. **Document zoom functionality** allows to zoom documents inside template. Allowed options: Fit, 50%, 75%, 100%, 125%, 150%, 200%
3. **Text heading** allows to set the text heading inside document (paragraph, cell). Allowed options: Paragraph, Header H1, Header H2, Header H3, Header H4
4. **Text font** allows to set text font inside document (paragraph, cell). Allowed options: Arial, Calibri, Courier New, Gergia, Roboto, Tahoma, Times New Roman, Verdana
5. **Text size** allows to set text size inside document (paragraph, cell). Allowed options: Tiny, Small, Default, Big, Huge
6. **Text styles** allows to apply styles to text, paragraph or cell. B - bold text style, I - italic text style, underscored U - underlined text style, underscored A - colored text, paint icon - colored background
7. **Text horizontal align** allows to apply horizontal text align in paragraph or cell. Allowed options: align left, align center, align right, justify text
8. **Add link** allows to insert link with custom text to the document :ref:`Link functionality documentation <addLinkTemplate>`
9. **Add image** allows to add image to hte document :ref:`Image functionality documentation <addImageTemplate>`
10. **Add table** allows to add static tables to the document. User is able to choose table columns and rows quantity. Max value is 10x10 :ref:`Static table documentation <addStaticTable>`
11. **Add list** allows to add list to the document. Allowed options: numbered list and bulleted list
12. **Page break** allows to set a mark after which new page will be started in the printed version of the document. In the digital version it is marked as a grey line
13. **Split document** allows to split document vertically on two equal parts. All content which has been added before applying split option will be added to the left part of the document
14. **Document options** allows to open context menu with document options. Allowed options: Clone, Delete, Page size, Page orientation
15. **Right side bar menu** allows to add :ref:`dynamic fields <fields>`, configure template details and template flow. Menu opens by click or opened by default for screen resolution bigger than 1920p
16. **Document editor area** where you can add text, images, tables and dynamic fields

---------------------------------

**Content list**

.. toctree::

    structuredDocument/structuredDocument.rst
    externalDocument/externalDocument.rst
    pdfDocument/pdfDocument.rst
    fields/fields.rst