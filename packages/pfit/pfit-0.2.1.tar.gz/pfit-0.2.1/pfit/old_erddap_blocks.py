
    
ERDDAP_BLOCK = XMLchunk = """
        {ERDDAP_HEADER}

        <addAttributes>
            <att name="creator_type">person</att>
            <att name="creator_url">https://webapps.nwtgeoscience.ca/WebAppsV2/Searching/ReferenceSearch.aspx</att>
            <att name="history">{B["Drilling method"]} drilling by {B["Collecting organization"]} (Project #{B["Project number"]}).</att>
            <att name="infoUrl">https://webapps.nwtgeoscience.ca/WebAppsV2/Searching/ReferenceSearch.aspx</att>
            <att name="license">The use of the published data will not carry restrictions. Full citation of referenced publications and reports by users is required.</att>
            <att name="sourceUrl">(local files)</att>
            <att name="standard_name_vocabulary">CF Standard Name Table v55</att>
            <att name="summary">Ground temperature for {borehole_id}.</att>
            <att name="title">Cryostratigraphic data for borehole {borehole_id}</att>
        </addAttributes>
        <dataVariable>
            <sourceName>latitude</sourceName>
            <destinationName>latitude</destinationName>
            <dataType>float</dataType>

            <addAttributes>
                <att name="colorBarMaximum" type="double">90.0</att>
                <att name="colorBarMinimum" type="double">-90.0</att>
                <att name="ioos_category">Location</att>
                <att name="long_name">Latitude</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>longitude</sourceName>
            <destinationName>longitude</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="colorBarMaximum" type="double">180.0</att>
                <att name="colorBarMinimum" type="double">-180.0</att>
                <att name="ioos_category">Location</att>
                <att name="long_name">Longitude</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>time</sourceName>
            <destinationName>time</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="ioos_category">Time</att>
                <att name="long_name">Time</att>
                <att name="units">days since 1990-01-01T00:00:00Z</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>borehole</sourceName>
            <destinationName>borehole</destinationName>
            <dataType>String</dataType>
            <addAttributes>
                <att name="ioos_category">Identifier</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>depth</sourceName>
            <destinationName>depth</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="bounds">null</att>
                <att name="colorBarMaximum" type="double">8000.0</att>
                <att name="colorBarMinimum" type="double">-8000.0</att>
                <att name="colorBarPalette">TopographyDepth</att>
                <att name="ioos_category">Location</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>frozen</sourceName>
            <destinationName>frozen</destinationName>
            <dataType>int</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="coordinates">null</att>
                <att name="ioos_category">Soils</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>cryostructures</sourceName>
            <destinationName>cryostructures</destinationName>
            <dataType>String</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="coordinates">null</att>
                <att name="ioos_category">Unknown</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>visible_ice</sourceName>
            <destinationName>visible_ice</destinationName>
            <dataType>String</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="coordinates">null</att>
                <att name="ioos_category">Ice Distribution</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>ASTM_2488</sourceName>
            <destinationName>ASTM_2488</destinationName>
            <dataType>String</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="coordinates">null</att>
                <att name="ioos_category">Unknown</att>
                <att name="long_name">A description of the interval according to ASTM-2488</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>materials</sourceName>
            <destinationName>materials</destinationName>
            <dataType>String</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="coordinates">null</att>
                <att name="ioos_category">Unknown</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>organic_cover</sourceName>
            <destinationName>organic_cover</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="coordinates">null</att>
                <att name="ioos_category">Unknown</att>
                <att name="long_name">The thickness of the organic cover according to field borehole logs (if present)</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>top_of_interval</sourceName>
            <destinationName>top_of_interval</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="colorBarMaximum" type="double">8000.0</att>
                <att name="colorBarMinimum" type="double">-8000.0</att>
                <att name="colorBarPalette">TopographyDepth</att>
                <att name="ioos_category">Location</att>
            </addAttributes>
        </dataVariable>
        <dataVariable>
            <sourceName>bottom_of_interval</sourceName>
            <destinationName>bottom_of_interval</destinationName>
            <dataType>float</dataType>
            <addAttributes>
                <att name="_ChunkSizes">null</att>
                <att name="colorBarMaximum" type="double">8000.0</att>
                <att name="colorBarMinimum" type="double">-8000.0</att>
                <att name="colorBarPalette">TopographyDepth</att>
                <att name="ioos_category">Location</att>
            </addAttributes>
        </dataVariable>
    </dataset>
    """


ERDDAP_HEADER = """
        <dataset type="EDDTableFromNcCFFiles" datasetID="{dataset_id}" active="true">
        <reloadEveryNMinutes>10080</reloadEveryNMinutes>
        <updateEveryNMillis>10000</updateEveryNMillis>
        <fileDir>{fileDir}</fileDir>
        <fileNameRegex>{Path(fname).name}</fileNameRegex>
        <recursive>true</recursive>
        <pathRegex>.*</pathRegex>
        <metadataFrom>last</metadataFrom>
        <standardizeWhat>0</standardizeWhat>
        <sortFilesBySourceNames></sortFilesBySourceNames>
        <fileTableInMemory>false</fileTableInMemory>
        <accessibleViaFiles>false</accessibleViaFiles>
        """
