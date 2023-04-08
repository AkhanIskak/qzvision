import {Column, Entity, PrimaryGeneratedColumn} from "typeorm";

@Entity()
export class BusEntity{
    @PrimaryGeneratedColumn()
    id:number;
    @Column({})
    routeId:number;
    //id of particular bus indifferent to its route number
    //because there are multiple buses with same routeNumbers
    @Column()
    specificBusId:number
    @Column()
    passengerAmount:number;
}
