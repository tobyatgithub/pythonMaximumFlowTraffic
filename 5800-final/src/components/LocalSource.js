import React from "react";
import {
  MapContainer,
  Marker,
  Popup,
  TileLayer,
  Polyline,
} from "react-leaflet";

import { Icon } from "leaflet";
import "./local.css";
import * as parkData from "../data/vancouver-locations.json";
import * as symboLines from "../data/vancouver-symbol";
import * as resultsLines from "../data/vancouver-results.json";
import { Button } from "react-bootstrap";

const greenOptions = { fillcolor: "lime", color: "lime" };
const redOptions = { fillcolor: "red", color: "red" };

const symbolNameMap = new Map();
parkData.features.map((park) =>
  symbolNameMap.set(park.symbol, park.geometry.coordinates)
);
//{ "start": "A", "end": { "B": 26, "C": 34, "D": 28 } },
const linePositions = [];
symboLines.lines.map((line1) =>
  line1.end.map((end) =>
    linePositions.push([
      symbolNameMap.get(line1.start),
      symbolNameMap.get(end.name),
      end.weight,
    ])
  )
);

const linePositionsAfter = [];
resultsLines.results.map((line1) =>
  line1.end.map((end) =>
    linePositionsAfter.push([
      symbolNameMap.get(line1.start),
      symbolNameMap.get(end.name),
      end.weight,
    ])
  )
);

export const sheep = new Icon({
  iconUrl: "/richard.png",
  iconSize: [25, 25],
});

const LocalSource = () => {
  const [activePark, setActivePark] = React.useState(null);
  const [activeButton, setActiveButton] = React.useState(false);

  const handleClick = () => {
    setActiveButton(true);
  };
  console.log(symbolNameMap);

  return (
    <div className="rowC">
      <Button className="button" onClick={handleClick}>
        Run
      </Button>
      <MapContainer center={[49.247123, -123.1416102]} zoom={13}>
        {/* <Circle center={[49.247123, -123.1416102]} radius={400} color="red" /> */}
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
        />
        {parkData.features.map((park) => (
          <Marker
            key={park.name}
            position={[
              park.geometry.coordinates[0],
              park.geometry.coordinates[1],
            ]}
            onClick={() => {
              setActivePark(park);
            }}
            icon={sheep}
          />
        ))}
        {linePositions.map((l) => (
          // <PolylineDecorator patterns={arrow} positions={[l[0], l[1]]} />
          <Polyline
            // arrowheads
            pathOptions={greenOptions}
            positions={[l[0], l[1]]}
            weight={l[2] * 0.4}
            stroke="true"
            offset="100%"
          />
        ))}

        {activePark && (
          <Popup
            position={[
              activePark.geometry.coordinates[0],
              activePark.geometry.coordinates[1],
            ]}
            onClose={() => {
              setActivePark(null);
            }}
          >
            <div>
              <h2>{activePark.properties.NAME}</h2>
              <p>{activePark.properties.DESCRIPTIO}</p>
            </div>
          </Popup>
        )}
        {activeButton &&
          linePositionsAfter.map((l) => (
            // <PolylineDecorator patterns={arrow} positions={[l[0], l[1]]} />
            <Polyline
              // arrowheads
              pathOptions={redOptions}
              positions={[l[0], l[1]]}
              weight={l[2] * 0.2}
              stroke="true"
              offset="100%"
            />
          ))}
      </MapContainer>
    </div>
  );
};

export default LocalSource;
